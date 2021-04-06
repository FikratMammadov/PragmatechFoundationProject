// SHOP PAGE Products image hover olduqda dəyişən şəkil

let cakeImageContainer = document.querySelector('.products .cake-item-img');
let cakeImageContainerWidth = cakeImageContainer.clientWidth;
let cakeImagesOverlay = document.querySelectorAll('.products .cake-item-img-overlay')
let cakeImages = document.querySelectorAll(".products .cake-item-img img")
let pos = 0;

for (let i = 0; i < cakeImages.length; i++) {
    cakeImages[i].style.width = `${cakeImageContainerWidth}px`;
    
    cakeImages[i].addEventListener('mouseover', function (e) {
        pos -= cakeImageContainerWidth;
        cakeImages[i].parentElement.parentElement.style.transform = `translateX(${pos}px)`;
    });



    cakeImages[i].addEventListener('mouseout', function (e) {
        // if (e.target.className != cakeImages[i].parentElement.nextElementSibling.className) {
            pos += cakeImageContainerWidth;
            cakeImages[i].parentElement.parentElement.style.transform = `translateX(${pos}px)`;
        // } 
    });



}
 

function checkStatus() {
    cakeImageContainerWidth = cakeImageContainer.clientWidth;
    for (let i = 0; i < cakeImages.length; i++) {
        cakeImages[i].style.width = `${cakeImageContainerWidth}px`;
    }
}

// products add to card button 

