/* Imaan Rafiq — portfolio interactions */
(function () {
  "use strict";

  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------- current year */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------------------------------------------------------- mobile menu */
  var toggle = document.querySelector(".nav__toggle");
  var menu = document.getElementById("menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.getAttribute("data-open") === "true";
      menu.setAttribute("data-open", open ? "false" : "true");
      toggle.setAttribute("aria-expanded", open ? "false" : "true");
      document.body.style.overflow = open ? "" : "hidden";
    });
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menu.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------------------------------------------------------- scroll state */
  var nav = document.querySelector(".nav");
  var bar = document.querySelector(".progress");
  var ticking = false;
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (nav) nav.setAttribute("data-scrolled", y > 24 ? "true" : "false");
    if (bar) {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? (y / h) * 100 : 0) + "%";
    }
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  /* ---------------------------------------------------------- reveal */
  var revealables = document.querySelectorAll("[data-reveal]");
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---------------------------------------------------------- work filter */
  var filters = document.querySelectorAll(".chip");
  var grid = document.querySelector("[data-grid]");
  if (filters.length && grid) {
    var cards = Array.prototype.slice.call(grid.querySelectorAll(".card"));
    var empty = document.querySelector("[data-empty]");
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var key = btn.getAttribute("data-filter");
        filters.forEach(function (b) { b.classList.toggle("is-active", b === btn); });
        var shown = 0;
        cards.forEach(function (c) {
          var tags = (c.getAttribute("data-tags") || "").split(/\s+/);
          var match = key === "all" || tags.indexOf(key) !== -1;
          c.hidden = !match;
          if (match) shown++;
        });
        if (empty) empty.hidden = shown !== 0;
      });
    });
  }

  /* ---------------------------------------------------------- lightbox */
  var lb = document.querySelector("[data-lightbox]");
  var shots = Array.prototype.slice.call(document.querySelectorAll("[data-full]"));
  if (lb && shots.length) {
    var imgEl = lb.querySelector("[data-lightbox-img]");
    var capEl = lb.querySelector("[data-lightbox-cap]");
    var closeBtn = lb.querySelector(".lightbox__close");
    var prevBtn = lb.querySelector(".lightbox__nav--prev");
    var nextBtn = lb.querySelector(".lightbox__nav--next");
    var index = 0;

    function show(i) {
      index = (i + shots.length) % shots.length;
      var s = shots[index];
      imgEl.src = s.getAttribute("data-full");
      imgEl.alt = s.getAttribute("data-cap") || "";
      capEl.textContent = s.getAttribute("data-cap") || "";
    }
    function open(i) {
      show(i);
      lb.hidden = false;
      lb.setAttribute("data-open", "");
      document.body.style.overflow = "hidden";
      closeBtn.focus();
    }
    function close() {
      lb.hidden = true;
      lb.removeAttribute("data-open");
      document.body.style.overflow = "";
    }
    shots.forEach(function (s, i) {
      s.addEventListener("click", function () { open(i); });
    });
    if (closeBtn) closeBtn.addEventListener("click", close);
    if (prevBtn) prevBtn.addEventListener("click", function () { show(index - 1); });
    if (nextBtn) nextBtn.addEventListener("click", function () { show(index + 1); });
    lb.addEventListener("click", function (ev) { if (ev.target === lb) close(); });
    document.addEventListener("keydown", function (ev) {
      if (lb.hidden) return;
      if (ev.key === "Escape") close();
      else if (ev.key === "ArrowLeft") show(index - 1);
      else if (ev.key === "ArrowRight") show(index + 1);
    });
  }
})();
