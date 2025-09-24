from django.urls import path

from . import views

urlpatterns = [
    path("/", views.HomePageView.as_view(), name="home"),
    path("catalog/", views.CatalogListView.as_view(), name="catalog"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/", views.ProductCreateView.as_view(), name="add_product"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("submit-form/", views.handle_form_submission, name="submit_form"),
]
