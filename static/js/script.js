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

// swiper js code===============

var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    loop: true,
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 200,
        modifier: 1,
        slideShadows: true,
    },
    pagination: {
        el: ".swiper-pagination",
    },
});


// gsap code----------------------------
let tl = gsap.timeline()

tl.from(".logo-part", {
    opacity: 0,
    duration: .3,
    delay: .5,
    y: -20,
})

tl.from(".link", {
    opacity: 0,
    duration: .5,
    y: -20,
    stagger: .05,
})

gsap.from(".lower-text-container h3,.header-text-container h1", {
    opacity: 0,
    duration: 1,
    delay: .3,
    y: -30,
    stagger: .1,
})

gsap.from(".info-link-1 a", {
    opacity: 0,
    duration: .7,
    delay: .6,
    x: -70,
})

// gsap.from(".info-card", {
//     opacity: 0,
//     scale: .2,
//     duration: 1,
//     scrollTrigger:{
//         trigger:".service-card-section .info-card",
//         scroller:"body",
//         // markers:true,
//         start:"top 80%",
//         end:"top 60%",
//         scrub:.5,
//     }
// })

let tl2 = gsap.timeline()

tl2.from(".about-banner-head h1,.about-banner-head h4", {
    opacity: 0,
    duration: 1,
    y: -30,
    delay: .3,
    stagger: .1,
})