// 1) Menu hambuerguesa responsive
const btnMenu = document.getElementById('btnMenu');
    const menuPrincipal = document.getElementById('menuPrincipal');

    btnMenu.addEventListener('click', () => {
        menuPrincipal.classList.toggle('activo');
        btnMenu.textContent = menuPrincipal.classList.contains('activo') ? '✕ Cerrar' : '☰ Menú';
    });

    document.querySelectorAll('nav a').forEach(enlace => {
        enlace.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                menuPrincipal.classList.remove('activo');
                btnMenu.textContent = '☰ Menú';
            }
        });
});

