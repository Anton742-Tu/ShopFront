// Функция для активации пункта меню
function activateMenuItem() {
    const currentPage = window.location.pathname.split('/').pop();

    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        link.classList.remove('text-white');
        link.classList.add('text-white-50');
    });

    // Определяем активную страницу по URL
    let activeLinkId = null;

    if (currentPage === 'index.html' || currentPage === '') {
        activeLinkId = 'menu-home';
    } else if (currentPage === 'catalog.html') {
        activeLinkId = 'menu-catalog'; // ID ссылки на Каталог
    } else if (currentPage === 'category.html') {
        activeLinkId = 'menu-category'; // Или создай отдельный ID для category
    } else if (currentPage === 'contacts.html') {
        activeLinkId = 'menu-contacts';
    }

    // Активируем найденную ссылку
    if (activeLinkId) {
        const link = document.getElementById(activeLinkId);
        if (link) {
            link.classList.add('active', 'text-white');
            link.classList.remove('text-white-50');
        }
    }
}

document.addEventListener('DOMContentLoaded', activateMenuItem);
