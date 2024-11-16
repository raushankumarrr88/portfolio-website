if (history.scrollRestoration) {
    history.scrollRestoration = "manual";
}

window.onload = function() {
    window.scrollTo(0, 0);

    const currentUrl = window.location.href;
    const menuItems = document.querySelectorAll(".navbar a");

    menuItems.forEach(function (menuItem) {
        if (menuItem.href === currentUrl) {
            menuItem.classList.add("active");
        }
    });
};

document.addEventListener("DOMContentLoaded", function () {
    const firstBlock = document.querySelector(
        ".main-container-main-page .main-container:first-of-type"
    );
    if (firstBlock) {
        const h3Name = firstBlock.querySelector(".h3-name");
        if (h3Name) {
            h3Name.classList.add("rainbow-text");
        }
    }

    const menuIcon = document.getElementById("menu-icon");
    const navbarItems = document.querySelectorAll('.navbar-item');
    const currentUrl = window.location.href;

    navbarItems.forEach(item => {
        if (item.href === currentUrl) {
            menuIcon.textContent = item.textContent;
        }
    });
});
