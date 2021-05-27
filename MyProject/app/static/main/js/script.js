// Home Page - home-slider section slider
let homeSliderHeader = document.querySelector('.home-slider-content-position h2');
let homeSliderDescription = document.querySelector('.home-slider-content-position h3');
let homeSliderPrice = document.querySelector(".home-slider-content-position p span");
let homeSliderBtn = document.querySelector(".home-slider-content-position a");
let homeSliderItem = document.querySelector('.home-slider-item');
let homeSliderPosition = document.querySelector('.home-slider-content-position');
let homeSliderBtnLeft = document.querySelector('.home-slider-buttons .fa-chevron-left');
let homeSliderBtnRight = document.querySelector('.home-slider-buttons .fa-chevron-right');
let homeSliderIndex = 0;
homeSliderContents = [
    {
        bgLink: "static/main/img/cake-3_2000x.jpg",
        header: "Fresh Cakes",
        descriptionColor: "rgb(252, 206, 123)",
        price: 50,
        btnColor: ('rgb(231, 101, 36)'),
        btnBgColor: "white"
    },
    {
        bgLink: "static/main/img/home-slider-bg-3.jpg",
        header: "Cup Cakes",
        descriptionColor: "rgb(252, 206, 123)",
        price: 60,
        btnColor: "rgb(226, 53, 68)",
        btnBgColor: "white"

    },
    {
        bgLink: "static/main/img/home-slider-bg-2.jpg",
        header: "Birthday Cakes",
        descriptionColor: "rgb(226, 53, 68)",
        price: 70,
        btnColor: "rgb(226, 53, 68)",
        btnBgColor: "white"
    }

];

homeSliderBtnLeft.addEventListener('click', function () {
    homeSliderIndex--;
    if (homeSliderIndex < 0) {
        homeSliderIndex = homeSliderContents.length - 1;
    }
    setHomeSliderContent();

    console.log(homeSliderIndex);
});

homeSliderBtnRight.addEventListener('click', function () {
    homeSliderIndex++;
    if (homeSliderIndex > homeSliderContents.length - 1) {
        homeSliderIndex = 0;
    }
    setHomeSliderContent();

    console.log(homeSliderIndex);
});

function setHomeSliderContent(){
    homeSliderHeader.textContent = homeSliderContents[homeSliderIndex].header;
    homeSliderDescription.style.color = homeSliderContents[homeSliderIndex].descriptionColor;
    homeSliderPrice.textContent = homeSliderContents[homeSliderIndex].price;
    homeSliderBtn.style.color = homeSliderContents[homeSliderIndex].btnColor;
    homeSliderBtn.style.backgroundColor = homeSliderContents[homeSliderIndex].btnBgColor;
    homeSliderItem.style.backgroundImage = `url(${homeSliderContents[homeSliderIndex].bgLink})`;
    if (homeSliderIndex == homeSliderContents.length - 1) {
        homeSliderPosition.style.float = 'right'
    } else {
        homeSliderPosition.style.float = 'left'
    }
    console.log(homeSliderPosition);
}

// console.log(homeSliderBtn.style.className);

// natureTaste section'da slider 
let natureTasteSliderContainer = document.querySelector('#natureTaste .slider ');
let natureTasteSliderContainerWidth = natureTasteSliderContainer.clientWidth;
let natureTasteContents = document.querySelectorAll('#natureTaste .slider .container-full');
let natureTasteSliderContent = document.querySelector('#natureTaste .slider .slider-contents');
let natureTasteLeftBtn = document.querySelector('#natureTaste .slider .btn-1');
let natureTasteRightBtn = document.querySelector("#natureTaste .slider .btn-2");
let pos=0;
let natureTasteIndex=0;

for(let i=0;i<natureTasteContents.length;i++){
    natureTasteContents[i].style.width = natureTasteSliderContainerWidth+"px";
}

natureTasteSliderContent.style.width = natureTasteSliderContainerWidth * natureTasteContents.length + 'px';
 
function checkSize(){
    // natureTaste section'da slider 
    natureTasteSliderContainerWidth = natureTasteSliderContainer.clientWidth;
    for(let i=0;i<natureTasteContents.length;i++){
        natureTasteContents[i].style.width = natureTasteSliderContainerWidth+"px";
    }
    natureTasteSliderContent.style.width = natureTasteSliderContainerWidth * natureTasteContents.length + 'px';
    

    // features section'da slider
    logosContainerWidth = logosContainer.clientWidth
    for(let i=0;i<logoItems.length;i++){
        logoItems[i].style.width=`${logosContainerWidth/5}px`
    }
}

natureTasteLeftBtn.addEventListener("click",function(){   
    if(natureTasteIndex>0){
        natureTasteIndex--;
        pos+=natureTasteSliderContainerWidth;
        natureTasteSliderContent.style.transform = `translateX(${pos}px)`;
        console.log(natureTasteIndex)
    }
})
natureTasteRightBtn.addEventListener('click',function(){
    if (natureTasteIndex < natureTasteContents.length - 1){
        natureTasteIndex++;
        pos-=natureTasteSliderContainerWidth;
        natureTasteSliderContent.style.transform = `translateX(${pos}px)`;
        console.log(natureTasteContents[natureTasteIndex-1]);
        console.log(natureTasteIndex)
    }
})

// features section'da slider

let logosContainer = document.querySelector('#features .logos');
let logosContainerWidth = logosContainer.clientWidth
let logoContent = document.querySelector('#features .logo-items')
let logoItems = document.querySelectorAll('#features .logo-item');
let logosLeftBtn=document.querySelector('#features .logos .btn-1');
let logosRightBtn=document.querySelector('#features .logos .btn-2')
let logoIndex=5
let logoPos=0

for(let i=0;i<logoItems.length;i++){
    logoItems[i].style.width=`${logosContainerWidth/5}px`
}

logosLeftBtn.addEventListener('click',function(){
    if(logoIndex>5){
        logoIndex--;
        pos+=logosContainerWidth/5
        logoContent.style.transform=`translateX(${pos}px)`;
    }
    console.log(logoIndex)
});

logosRightBtn.addEventListener('click',function(){
    if(logoIndex<=logoItems.length-1){
        logoIndex++;
        pos-=logosContainerWidth/5
        logoContent.style.transform=`translateX(${pos}px)`;
    }
    console.log(logoIndex)
})
 
// console.log(logoItem)


// asked section'da accordion

function toggleAccordion(elem) {
    nextElement = elem.nextElementSibling;
    askedContents = elem.parentElement.parentElement;
    btn = elem.children[1].children[0]
    // Eger paragraf gorunurse toggle status true , eks halda false olsun
    if (nextElement.className == "question-answer show") {
        toggleStatus = true;
    } else {
        toggleStatus = false;
    }

    if (toggleStatus == false) {
        for (let i = 0; i < askedContents.children.length; i++) {
            askedContents.children[i].children[1].className = "question-answer hide"
            askedContents.children[i].children[0].children[1].children[0].className = "fal fa-plus"
        }
        nextElement.className = "question-answer show";
        btn.className = "fal fa-minus"
    }

}


 



