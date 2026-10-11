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

// ===========================
// Dropdown Navigation
// ===========================
const dropdownToggles = document.querySelectorAll('.nav-dropdown-toggle');
const dropdownItems = document.querySelectorAll('.nav-item-dropdown');

dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        e.preventDefault();
        const parent = toggle.closest('.nav-item-dropdown');
        const isOpen = toggle.getAttribute('aria-expanded') === 'true';
        closeAllDropdowns();
        if (!isOpen) {
            parent.classList.add('active');
            toggle.setAttribute('aria-expanded', 'true');
            parent.querySelector('.nav-dropdown').classList.add('active');
        }
    });

    toggle.addEventListener('keydown', (e) => {
        const parent = toggle.closest('.nav-item-dropdown');
        const dropdown = parent.querySelector('.nav-dropdown');
        const links = dropdown.querySelectorAll('a');

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            const isOpen = toggle.getAttribute('aria-expanded') === 'true';
            if (!isOpen) {
                parent.classList.add('active');
                toggle.setAttribute('aria-expanded', 'true');
                dropdown.classList.add('active');
            }
            if (links.length > 0) links[0].focus();
        } else if (e.key === 'Escape') {
            closeAllDropdowns();
            toggle.focus();
        }
    });
});

document.querySelectorAll('.nav-dropdown-link').forEach(link => {
    link.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeAllDropdowns();
            const toggle = link.closest('.nav-item-dropdown').querySelector('.nav-dropdown-toggle');
            toggle.focus();
        }
    });

    link.addEventListener('click', () => {
        closeAllDropdowns();
        navMenu.classList.remove('active');
    });
});

function closeAllDropdowns() {
    dropdownItems.forEach(item => {
        item.classList.remove('active');
        const toggle = item.querySelector('.nav-dropdown-toggle');
        const dropdown = item.querySelector('.nav-dropdown');
        toggle.setAttribute('aria-expanded', 'false');
        dropdown.classList.remove('active');
    });
}

document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-item-dropdown') && !e.target.closest('.nav-dropdown-toggle')) {
        closeAllDropdowns();
    }
});

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
// Homepage Chart, Reveal & Counter Animations
// ===========================
(function(){
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var trend = document.getElementById('trend');
  if (trend && trend.getTotalLength) {
    trend.style.setProperty('--len', Math.ceil(trend.getTotalLength()));
  }

  if (reduce || !('IntersectionObserver' in window)) return;
  root.classList.add('motion');

  // Section reveal: only items still below the fold start hidden, so the first view is always complete.
  var items = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  var vh = window.innerHeight;
  items.forEach(function(el){
    if (el.getBoundingClientRect().top > vh) el.classList.add('pending');
  });
  var cards = document.querySelectorAll('.card.reveal');
  Array.prototype.forEach.call(cards, function(c, i){
    c.style.transitionDelay = (i * 100) + 'ms';
  });
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting){
        e.target.classList.remove('pending');
        e.target.classList.add('active');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.15 });
  items.forEach(function(el){
    if (el.classList.contains('pending')) io.observe(el);
    else el.classList.add('active');
  });

  // Count up once when the number scrolls into view.
  var counters = document.querySelectorAll('.count');
  var co = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (!e.isIntersecting) return;
      co.unobserve(e.target);
      var el = e.target, to = +el.getAttribute('data-to'), start = null, dur = 1200;
      function step(t){
        if (start === null) start = t;
        var p = Math.min((t - start) / dur, 1);
        el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(step);
      }
      el.textContent = '0';
      requestAnimationFrame(step);
    });
  }, { threshold: 0.6 });
  Array.prototype.forEach.call(counters, function(c){ co.observe(c); });
})();

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
            const categories = (card.dataset.category || '').toLowerCase().split(/\s+/);
            const matches = filter === 'all' || categories.includes(filter.toLowerCase());
            card.classList.toggle('hidden', !matches);
        });
    });
});

// ===========================
// Read More / Less (Publications)
// ===========================
document.querySelectorAll('.read-more-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const fullDetails = btn.previousElementSibling;
        if (!fullDetails) return;
        const summary = fullDetails.previousElementSibling;
        const isCollapsed = fullDetails.classList.contains('collapsed');
        fullDetails.classList.toggle('collapsed', !isCollapsed);
        fullDetails.classList.toggle('expanded', isCollapsed);
        if (summary && summary.classList.contains('pub-summary')) {
            summary.style.display = isCollapsed ? 'none' : '';
        }
        btn.textContent = isCollapsed ? 'Read less ▴' : 'Read more ▾';
        btn.setAttribute('aria-expanded', isCollapsed ? 'true' : 'false');
    });
});

// ===========================
// Accessible Book Card Flip
// ===========================
document.querySelectorAll('.book-flip-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const card = btn.closest('.flip-card');
        if (card) card.classList.add('flipped');
    });
});

document.querySelectorAll('.book-flip-back-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const card = btn.closest('.flip-card');
        if (card) card.classList.remove('flipped');
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
