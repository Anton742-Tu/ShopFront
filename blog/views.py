from django.contrib import messages
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BlogPostForm
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        """Фильтрация опубликованных статей"""
        return BlogPost.objects.filter(is_published=True).order_by("-created_at")


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        """Увеличение счетчика просмотров при открытии статьи"""
        obj = super().get_object(queryset)

        # Увеличиваем счетчик просмотров атомарно
        BlogPost.objects.filter(pk=obj.pk).update(views_count=F("views_count") + 1)

        # Обновляем объект для отображения актуального счетчика
        obj.refresh_from_db()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        """Обработка успешного создания записи"""
        messages.success(self.request, "Запись успешно создана!")
        return super().form_valid(form)

    def get_success_url(self):
        """Перенаправление на созданную статью"""
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.object.slug})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/post_form.html"
    slug_url_kwarg = "slug"

    def form_valid(self, form):
        """Обработка успешного редактирования записи"""
        messages.success(self.request, "Запись успешно обновлена!")
        return super().form_valid(form)

    def get_success_url(self):
        """Перенаправление на отредактированную статью"""
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/post_confirm_delete.html"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("blog:post_list")

    def delete(self, request, *args, **kwargs):
        """Обработка успешного удаления записи"""
        messages.success(self.request, "Запись успешно удалена!")
        return super().delete(request, *args, **kwargs)


# Дополнительный контроллер для управления записями (только для staff)
class BlogPostManageListView(ListView):
    """Список всех записей (включая неопубликованные) для управления"""

    model = BlogPost
    template_name = "blog/post_manage_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        """Все записи для администраторов"""
        return BlogPost.objects.all().order_by("-created_at")

    def dispatch(self, request, *args, **kwargs):
        """Проверка прав доступа"""
        if not request.user.is_staff:
            messages.error(request, "У вас нет прав для доступа к этой странице.")
            return redirect("blog:post_list")
        return super().dispatch(request, *args, **kwargs)
