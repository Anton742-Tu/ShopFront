from django.urls import path
from .views import (
    HomePageView,
    ProductDetailView,
    CatalogListView,
    ProductCreateView,
    ContactsView,
    handle_form_submission,
    CategoryView
)

urlpatterns = [
    # Class-Based Views
    path('', HomePageView.as_view(), name='home'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/', CategoryView.as_view(), name='category'),

    # Function-Based View (оставляем для формы)
    path('submit-form/', handle_form_submission, name='submit_form'),
]
