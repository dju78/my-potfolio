// ===========================
// Navigation
// ===========================
const navbar    = document.getElementById('navbar');
const navToggle = document.getElementById('navToggle');
const navMenu   = document.getElementById('navMenu');
const navLinks  = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });

navToggle.addEventListener('click', () => {
    const open = navMenu.classList.toggle('active');
    navToggle.setAttribute('aria-expanded', open);
});

navLinks.forEach(link => link.addEventListener('click', () => navMenu.classList.remove('active')));

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');

function setActiveNav() {
    let current = '';
    sections.forEach(s => {
        if (window.scrollY >= s.offsetTop - 220) current = s.id;
    });
    navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
    });
}
window.addEventListener('scroll', setActiveNav, { passive: true });

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) window.scrollTo({ top: target.offsetTop - 72, behavior: 'smooth' });
    });
});

// ===========================
// Reveal on Scroll
// ===========================
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ===========================
// Counter Animation
// ===========================
function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    if (isNaN(target)) return;

    const duration = 1800;
    const start = performance.now();

    function update(now) {
        const progress = Math.min((now - start) / duration, 1);
        const eased    = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target) + suffix;
        if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
}

// Observe the metrics strip (new dashboard counters)
const metricsStrip = document.querySelector('.metrics-strip');
if (metricsStrip) {
    new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.querySelectorAll('.metric-number[data-target]').forEach(animateCounter);
            }
        });
    }, { threshold: 0.4 }).observe(metricsStrip);
}

// ===========================
// Project Filter Tabs
// ===========================
const filterBtns   = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.dataset.filter;
        projectCards.forEach(card => {
            const cat = card.dataset.category || '';
            card.classList.toggle('hidden', filter !== 'all' && cat !== filter);
        });
    });
});

// ===========================
// Read More / Less (Publications)
// ===========================
document.querySelectorAll('.read-more-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const desc = btn.previousElementSibling;
        if (!desc) return;
        const isCollapsed = desc.classList.contains('collapsed');
        desc.classList.toggle('collapsed', !isCollapsed);
        desc.classList.toggle('expanded', isCollapsed);
        btn.textContent = isCollapsed ? 'Read less ▴' : 'Read more ▾';
        btn.setAttribute('aria-expanded', isCollapsed ? 'true' : 'false');
    });
});

// ===========================
// Timeline hover
// ===========================
document.querySelectorAll('.timeline-item').forEach(item => {
    const marker = item.querySelector('.timeline-marker');
    if (!marker) return;
    item.addEventListener('mouseenter', () => marker.style.transform = 'scale(1.3)');
    item.addEventListener('mouseleave', () => marker.style.transform = '');
});

// ===========================
// Footer Year
// ===========================
const footerYear = document.getElementById('footer-year');
if (footerYear) footerYear.textContent = new Date().getFullYear();

// ===========================
// Page Load Fade-In
// ===========================
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.4s ease';
    requestAnimationFrame(() => requestAnimationFrame(() => { document.body.style.opacity = '1'; }));
});
