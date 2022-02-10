document.addEventListener('DOMContentLoaded', () => {
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
        const $notification = $delete.parentNode;

        $delete.addEventListener('click', () => {
            $notification.parentNode.removeChild($notification);
        });
    });
});

// code from Bulma GitHub to fix the navbar menu always open on mobile 
// https://github.com/jgthms/bulma/issues/2361
document.addEventListener("DOMContentLoaded", () => {
    const hamburgerButton = document.querySelector(".navbar-burger");
    const navMenu = document.querySelector(".navbar-menu");

    hamburgerButton.addEventListener("click", () => {
        hamburgerButton.classList.toggle("is-active");
        navMenu.classList.toggle("is-active");
    });

    const allDropdowns = document.querySelectorAll(
        ".navbar-item.has-dropdown.is-hoverable.mobile"
    );

    allDropdowns.forEach((dropdown) => {
        dropdown.addEventListener("click", () => {
            const elem = dropdown.querySelector(".navbar-dropdown");
            elem.classList.toggle("is-active");
        });
    });
});
$(document).ready(function () {
    // Initialize Uni-Form
    $(function () {
        $('form.uniForm').uniform();
    });
});