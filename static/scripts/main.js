// const searchInput = document.querySelector("#search");
const searchButton = document.querySelector(".topnav button");
// const test = document.querySelector("#")

searchButton.addEventListener("click", () => {
    searchInput.classList.toggle("expanded");
    searchInput.focus();
});
let menu = document.querySelector(".navbar");
document.querySelector("#menu-icon").onclick = () => {
    menu.classList.toggle("active");
}
let header = document.quesrySelector("header");

window.addEventListener("scroll" ,() =>{
    header.classList.toggle("shadow", window.scrollY > 0);
});

