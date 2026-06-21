document.addEventListener('DOMContentLoaded', () => {
    const yearElement = document.getElementById('current-year');

    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }

    const navbarCollapse = document.getElementById('mainNavbar');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach((link) => {
        link.addEventListener('click', () => {
            if (navbarCollapse && navbarCollapse.classList.contains('show') && window.bootstrap) {
                window.bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();
            }
        });
    });

    document.querySelectorAll('.needs-validation').forEach((form) => {
        form.addEventListener('submit', (event) => {
            event.preventDefault();
            event.stopPropagation();

            if (form.checkValidity()) {
                form.reset();
                form.classList.remove('was-validated');
                return;
            }

            form.classList.add('was-validated');
        });
    });

    const animatedElements = document.querySelectorAll('[data-animate]');

    if (!('IntersectionObserver' in window)) {
        animatedElements.forEach((element) => element.classList.add('is-visible'));
        return;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.18 });

    animatedElements.forEach((element) => observer.observe(element));
});
