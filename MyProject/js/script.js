// Home Page - home-slider section slider
let homeSliderHeader = document.querySelector('.home-slider-content-position h2');
let homeSliderDescription = document.querySelector('.home-slider-content-position h3');
let homeSliderPrice = document.querySelector(".home-slider-content-position p span");
let homeSliderBtn = document.querySelector(".home-slider-content-position a");
let homeSliderItem = document.querySelector('.home-slider-item');
let homeSliderPosition = document.querySelector('.home-slider-content-position');
let homeSliderBtnLeft = document.querySelector('.home-slider-buttons .fa-chevron-left');
let homeSliderBtnRight = document.querySelector('.home-slider-buttons .fa-chevron-right');
let index = 0;
homeSliderContents = [
    {
        bgLink: "img/cake-3_2000x.jpg",
        header: "Fresh Cakes",
        descriptionColor: "rgb(252, 206, 123)",
        price: 50,
        btnColor: ('rgb(231, 101, 36)'),
        btnBgColor: "white"
    },
    {
        bgLink: "img/home-slider-bg-3.jpg",
        header: "Cup Cakes",
        descriptionColor: "rgb(252, 206, 123)",
        price: 60,
        btnColor: "rgb(226, 53, 68)",
        btnBgColor: "white"

    },
    {
        bgLink: "img/home-slider-bg-2.jpg",
        header: "Birthday Cakes",
        descriptionColor: "rgb(226, 53, 68)",
        price: 70,
        btnColor: "rgb(226, 53, 68)",
        btnBgColor: "white"
    }

];

homeSliderBtnLeft.addEventListener('click', function () {
    index--;
    if (index < 0) {
        index = homeSliderContents.length - 1;
    }
    setHomeSliderContent();

    console.log(index);
});

homeSliderBtnRight.addEventListener('click', function () {
    index++;
    if (index > homeSliderContents.length - 1) {
        index = 0;
    }
    setHomeSliderContent();

    console.log(index);
});

function setHomeSliderContent(){
    homeSliderHeader.textContent = homeSliderContents[index].header;
    homeSliderDescription.style.color = homeSliderContents[index].descriptionColor;
    homeSliderPrice.textContent = homeSliderContents[index].price;
    homeSliderBtn.style.color = homeSliderContents[index].btnColor;
    homeSliderBtn.style.backgroundColor = homeSliderContents[index].btnBgColor;
    homeSliderItem.style.backgroundImage = `url(${homeSliderContents[index].bgLink})`;
    if (index == homeSliderContents.length - 1) {
        homeSliderPosition.style.float = 'right'
    } else {
        homeSliderPosition.style.float = 'left'
    }
    console.log(homeSliderPosition);
}

// console.log(homeSliderBtn.style.className);

// natureTaste section'da slider 
let natureTasteSliderContainer = document.querySelector('#natureTaste .slider');
let natureTasteSliderContainerWidth = natureTasteSliderContainer.clientWidth;
let natureTasteContents = document.querySelectorAll('#natureTaste .slider .container-full');
let natureTasteSliderContent = document.querySelector('#natureTaste .slider .slider-contents');
let natureTasteLeftBtn = document.querySelector('#natureTaste .slider .btn-1');
let natureTasteRightBtn = document.querySelector("#natureTaste .slider .btn-2");
let pos=0;
index=0;

for(let i=0;i<natureTasteContents.length;i++){
    natureTasteContents[i].style.width = natureTasteSliderContainerWidth+"px";
    // console.log(natureTasteContents[i])
}

natureTasteLeftBtn.addEventListener("click",function(){   
    if(index>0){
        index--;
        pos+=natureTasteSliderContainerWidth;
        natureTasteSliderContent.style.transform = `translateX(${pos}px)`;
        console.log(index)
    }
})
natureTasteRightBtn.addEventListener('click',function(){
    if (index < natureTasteContents.length - 1){
        index++;
        pos-=natureTasteSliderContainerWidth;
        natureTasteSliderContent.style.transform = `translateX(${pos}px)`;
        console.log(natureTasteContents[index-1]);
        console.log(index)
    }
})



 



