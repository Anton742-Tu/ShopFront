// Функция для активации пункта меню в Django
function activateMenuItem() {
    // Получаем текущий URL путь
    const currentPath = window.location.pathname;

    // Убираем активный класс у всех пунктов меню
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        link.classList.remove('text-white');
        link.classList.add('text-white-50');
    });

    // Активируем нужный пункт меню в зависимости от пути
    const menuLinks = {
        '/': 'menu-home',
        '/catalog/': 'menu-catalog',
        '/category/': 'menu-category',
        '/contacts/': 'menu-contacts'
    };

    // Находим ID для текущего пути
    const linkId = menuLinks[currentPath];

    // Активируем найденную ссылку
    if (linkId) {
        const link = document.getElementById(linkId);
        if (link) {
            link.classList.add('active', 'text-white');
            link.classList.remove('text-white-50');
        }
    }
}

// Запускаем функцию при загрузке страницы
document.addEventListener('DOMContentLoaded', activateMenuItem);

// Также обновляем при переходе по истории браузера
window.addEventListener('popstate', activateMenuItem);
