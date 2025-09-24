from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Category, Contact
from .forms import ProductForm


class HomePageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 6
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Новинки'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f"\nПросмотр товара: {self.object.name} (ID: {self.object.id})")
        return context


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Каталог товаров'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        product = form.save()
        messages.success(self.request, f'Товар "{product.name}" успешно добавлен!')
        return redirect('product_detail', pk=product.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Добавить товар'
        return context


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        main_contact = Contact.objects.filter(is_main_contact=True, is_active=True).first()

        if main_contact and main_contact.person_name:
            contacts = Contact.objects.filter(
                person_name=main_contact.person_name,
                is_active=True
            ).order_by('order')
            page_title = main_contact.person_name
            show_person = True
        else:
            contacts = Contact.objects.filter(is_active=True).order_by('order')
            page_title = "Наши контакты"
            show_person = False

        context.update({
            'contacts': contacts,
            'page_title': page_title,
            'show_person': show_person
        })
        return context


class CategoryView(TemplateView):
    template_name = "category.html"


def handle_form_submission(request):
    """Обработка формы обратной связи"""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print("\n" + "=" * 50)
        print("НОВАЯ ЗАЯВКА С ФОРМЫ:")
        print(f"Имя: {name}")
        print(f"Email: {email}")
        print(f"Сообщение: {message}")
        print("=" * 50 + "\n")

        return render(request, "contacts.html", {"success": True})

    return render(request, "contacts.html")
