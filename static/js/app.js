document.addEventListener("DOMContentLoaded", () => {
  const menuBtn = document.getElementById("menu-btn");
  const mobileNav = document.getElementById("mobile-nav");

  menuBtn.addEventListener("click", () => {
    menuBtn.classList.toggle("open");
    mobileNav.classList.toggle("open");
  });
});
