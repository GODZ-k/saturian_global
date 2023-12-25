// navbar section -----------------------------------

var bar = document.getElementById("bar");
var close = document.getElementById("close");
var nav = document.getElementById("navbar");
if (bar) {
    bar.addEventListener("click", () => {
        nav.classList.add("active");
    })
}
if (close) {
    close.addEventListener("click", () => {
        nav.classList.remove("active");
    })
}

// popup after window load --------------------------------------

const popup = document.querySelector('.popup');
const x = document.querySelector('#close-popup')

window.addEventListener('load', () => {
    setTimeout(function open(event) {
        popup.classList.add('showPopup');
        popup.childNodes[1].classList.add('showPopup');
    }, 2000)

})
x.addEventListener('click', () => {
    popup.classList.remove('showPopup');
    popup.childNodes[1].classList.remove('showPopup');
})

// quotation form popup-------------------------------------------------