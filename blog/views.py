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
        return BlogPost.objects.filter(is_published=True).order_by("-created_at")


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Увеличиваем счетчик просмотров
        obj.views_count = F("views_count") + 1
        obj.save(update_fields=["views_count"])
        obj.refresh_from_db()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно создана!")
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/post_form.html"
    slug_url_kwarg = "slug"

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно обновлена!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/post_confirm_delete.html"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("blog:post_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Запись успешно удалена!")
        return super().delete(request, *args, **kwargs)
