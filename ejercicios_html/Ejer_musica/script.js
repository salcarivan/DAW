// script.js
document.addEventListener("DOMContentLoaded", function() {
    console.log("Sitio web Sonidos Metal cargado correctamente.");
    
    // Interacción básica: saludo al hacer clic en el encabezado
    const header = document.querySelector("header");
    if (header) {
        header.addEventListener("click", function() {
            alert("¡Bienvenido al mundo del Metal! Explora las bandas y su historia.");
        });
    }

    // Resaltar visualmente el enlace activo en la navegación
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll("nav a");
    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath.split("/").pop()) {
            link.style.backgroundColor = "#8b0000";
            link.style.color = "#fff";
        }
    });
});