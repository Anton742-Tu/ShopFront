from django.contrib import admin
from django.urls import include, path

from catalog.views import (
    catalog_page,
    category_page,
    contacts_page,
    handle_form_submission,
    home_page,
)

urlpatterns = [
    # Админка
    path("admin/", admin.site.urls),
    # Маршрут для домашней страницы
    path("", home_page, name="home"),
    # Маршрут для страницы контактов
    path("contacts/", contacts_page, name="contacts"),
    # Маршрут для обработки POST-запроса формы
    path("submit-form/", handle_form_submission, name="submit_form"),
    # Дополнительные маршруты
    path("catalog/", catalog_page, name="catalog"),
    path("category/", category_page, name="category"),
    path("", include("catalog.urls")),  # Подключаем URLs приложения catalog
]
