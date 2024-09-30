if (history.scrollRestoration) {
    history.scrollRestoration = 'manual';
}

window.onload = function() {
    window.scrollTo(0, 0);
};

document.addEventListener("DOMContentLoaded", function () {
    const currentUrl = window.location.href;
    const menuItems = document.querySelectorAll('.navbar a');

    menuItems.forEach(function (menuItem) {
        if (menuItem.href === currentUrl) {
            menuItem.classList.add('active');
        }
    });
});

