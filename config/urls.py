from django.contrib import admin
from django.urls import path
from catalog.views import home_page, contacts_page, handle_form_submission, catalog_page, category_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('catalog/', catalog_page, name='catalog'),
    path('category/', category_page, name='category'),
    path('contacts/', contacts_page, name='contacts'),
    path('submit-form/', handle_form_submission, name='submit_form'),
]
