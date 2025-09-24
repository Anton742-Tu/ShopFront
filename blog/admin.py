from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_published", "views_count")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        ("Основная информация", {"fields": ("title", "slug", "content")}),
        ("Медиа", {"fields": ("preview_image",)}),
        ("Дополнительно", {"fields": ("is_published", "views_count")}),
    )
