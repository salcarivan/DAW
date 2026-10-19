// 1) MENÚ HAMBURGUESA (RESPONSIVE)

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

// 2) ANIMACIÓN DE SECCIONES AL HACER SCROLL

const secciones = document.querySelectorAll('section');

const observador = new IntersectionObserver((entradas) => {
    entradas.forEach(entrada => {
        if (entrada.isIntersecting) {
            entrada.target.classList.add('visible');
        }
    });
}, { threshold: 0.15 });

secciones.forEach(seccion => observador.observe(seccion));

// 3) BOTÓN "VOLVER ARRIBA"

const btnTop = document.getElementById('btnTop');

window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
        btnTop.classList.add('visible');
    } else {
        btnTop.classList.remove('visible');
    }
});

btnTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// 4) CONTADOR DE ESPECTROS

const contador = document.getElementById('contador');
let numeroEspectros = 0;
const totalEspectros = 666;

setInterval(() => {
    if (numeroEspectros < totalEspectros) {
        numeroEspectros += Math.floor(Math.random() * 5) + 1;
        if (numeroEspectros > totalEspectros) numeroEspectros = totalEspectros;
        contador.textContent = numeroEspectros;
    }
}, 80);

// 5) FANTASMAS FLOTANTES DECORATIVOS

const emojisFantasma = ['👻', '🦇', '🕯️', '💀', '🎃'];

function crearFantasma() {
    const fantasma = document.createElement('div');
    fantasma.classList.add('fantasma-flotante');
    fantasma.textContent = emojisFantasma[Math.floor(Math.random() * emojisFantasma.length)];
    fantasma.style.left = Math.random() * 100 + 'vw';
    fantasma.style.top = Math.random() * 100 + 'vh';
    fantasma.style.fontSize = (Math.random() * 2 + 1.5) + 'rem';
    fantasma.style.animationDuration = (Math.random() * 10 + 10) + 's';
    document.body.appendChild(fantasma);

    setTimeout(() => fantasma.remove(), 20000);
}

for (let i = 0; i < 6; i++) {
    setTimeout(crearFantasma, i * 500);
}

setInterval(crearFantasma, 3000);

// 6) TARJETAS DE ACTORES EXPANDIBLES

document.querySelectorAll('.actor-card').forEach(card => {
    card.addEventListener('click', () => {
        card.classList.toggle('expandida');
    });
});

// 7) MENSAJE EN CONSOLA
console.log('%c🏨 Bienvenido al Hotel Undervale 👻', 
    'color: #e0aaff; font-size: 20px; background: #240046; padding: 10px; border-radius: 5px;');
console.log('%c"La muerte es solo el check-in..."', 
    'color: #c77dff; font-style: italic; font-size: 14px;');