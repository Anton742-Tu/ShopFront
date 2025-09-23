from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('catalog/', views.catalog_page, name='catalog'),
    path('category/', views.category_page, name='category'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('submit-form/', views.handle_form_submission, name='submit_form'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/add/', views.add_product, name='add_product'),
]
