/*  1. Butona klik etdirmek.
        - buton secilmelidir.
    2. butona click olunanda img src deyeri deyissin
*/

let leftBtn = document.querySelector('#btn-left');
let rightBtn = document.querySelector('#btn-right');
let slideImgSrc = document.querySelector('.slide-frame img')
let title=document.querySelector('.desc p');
let index = 0;


console.log(title);
slides=[
    {
        img:"img/slide-img-1.jpg",
        title:"Birinci seklin aciqlamsi"
    },
    {
        img:"img/slide-img-2.jpg",
        title:"Ikinci seklin aciqlamsi"
    },
    {
        img:"img/slide-img-3.jpg",
        title:"Ucuncu seklin aciqlamsi"
    }
]

imgs = ["img/slide-img-1.jpg", "img/slide-img-2.jpg", "img/slide-img-3.jpg"]

titleTexts = [
    "Birinci seklin aciqlamsi",
    "Ikinci seklin aciqlamsi",
    "Ucuncu seklin aciqlamsi"
]
slideImgSrc.setAttribute('src', slides[0].img)
title.innerHTML=slides[0].title;
// events

leftBtn.addEventListener('click', function () {
    if (index > 0) {
        index--;
        slideImgSrc.setAttribute('src', slides[index].img)
        title.innerHTML=slides[index].title;
        console.log(index)
    }
     
})

rightBtn.addEventListener('click', function () {
    if (index < slides.length-1) {
        index++;
        slideImgSrc.setAttribute('src', slides[index].img)
        title.innerHTML=slides[index].title;
        console.log(index)
    }
})


