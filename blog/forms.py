from django import forms

from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content", "preview_image", "is_published"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите заголовок"}
            ),
            "slug": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Уникальный URL-адрес"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "Введите содержимое записи",
                }
            ),
            "preview_image": forms.FileInput(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title": "Заголовок",
            "slug": "URL-адрес",
            "content": "Содержимое",
            "preview_image": "Превью",
            "is_published": "Опубликовать",
        }
        help_texts = {
            "slug": "Уникальный идентификатор для URL (только латинские буквы, цифры, дефисы и подчеркивания)",
        }
