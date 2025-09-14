from django.shortcuts import render


def home_page(request):
    """Домашняя страница"""
    return render(request, 'index.html')


def contacts_page(request):
    """Страница контактов"""
    return render(request, 'contacts.html')


def handle_form_submission(request):
    """Обработка формы обратной связи"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print("\n" + "=" * 50)
        print("НОВАЯ ЗАЯВКА С ФОРМЫ:")
        print(f"Имя: {name}")
        print(f"Email: {email}")
        print(f"Сообщение: {message}")
        print("=" * 50 + "\n")

        return render(request, 'contacts.html', {'success': True})

    # Если GET-запрос, просто показываем форму
    return render(request, 'contacts.html')


def catalog_page(request):
    """Страница каталога"""
    return render(request, 'catalog.html')


def category_page(request):
    """Страница категории"""
    return render(request, 'category.html')
