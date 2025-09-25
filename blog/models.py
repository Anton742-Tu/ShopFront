from django.db import models
from django.urls import reverse
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок блоговой записи",
    )

    content = models.TextField(
        verbose_name="Содержимое", help_text="Введите текст блоговой записи"
    )

    preview_image = models.ImageField(
        upload_to="blog/previews/",
        verbose_name="Превью",
        help_text="Загрузите изображение для превью",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )

    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров',
        editable=False  # ← ЗАПРЕТ РУЧНОГО РЕДАКТИРОВАНИЯ
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="URL-адрес",
        help_text="Уникальный URL-адрес для записи",
    )

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    def increment_views(self):
        """Увеличивает счетчик просмотров"""
        self.views_count += 1
        self.save(update_fields=["views_count"])
