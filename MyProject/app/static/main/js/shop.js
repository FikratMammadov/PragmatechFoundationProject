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

let cardProductName = document.querySelector(".card-content-product-description-name");
let cardProductPrice = document.querySelector('.card-content-product-description-price');
let cardProductTotalPrice = document.querySelector(".card-pay-product-price");
let cardProductNumber = document.querySelector('.card-content-product-description-number');
let cardProductTotalNumber = document.querySelector('.card-pay-product-number')
let cardProductImage = document.querySelector('.card-content-product-image img');
let addToCartContainer = document.querySelector('.addToCart-overlay');
let addToCardItem = document.querySelector('.card-item');
let cardDeleteBtn = document.querySelector('.card-item-close')
let totalPrice = 0;
let totalNumber = 0;
let number = 0;

total = 0
function addToCart(e, num) {
    number += Number(num);
    addToCartContainer.style.display = "block";




    //total number
    totalNumber++;

    // total price
    totalPrice = totalPrice + Number(e.parentElement.children[1].childNodes[0].textContent.slice(1));

    // set product name
    cardProductName.textContent = e.parentElement.children[0].children[0].textContent;

    // set product price
    cardProductPrice.textContent = e.parentElement.children[1].childNodes[0].textContent;

    // set product total price
    cardProductTotalPrice.textContent = `$${total + Number(e.parentElement.children[1].childNodes[0].textContent.slice(1))}.00 USD`;

    // set product number
    cardProductNumber.textContent = `Qyt: ${1}`

    // set total product number
    cardProductTotalNumber.textContent = `there are ${cartItemNumber + 1} item(s) in your cart`

    // set product image
    cardProductImage.setAttribute('src', e.parentElement.previousElementSibling.children[0].children[0].children[0].src)


}



addToCartContainer.addEventListener('click', function (e) {
    if (e.target.className == addToCardItem.parentElement.parentElement.className) {
        addToCartContainer.style.display = "none";
    }
    else if (e.target.className == cardDeleteBtn.className || e.target.className == cardDeleteBtn.children[0].className) {
        addToCartContainer.style.display = "none";
    }
    else {
        addToCartContainer.style.display = "block";
    }
});



/*choices section'da category'də accordion*/

function choicesAccoridion(e) {
    choicesNextElement = e.parentElement.nextElementSibling;
    choicesBtn = e.children[0];

    if (choicesBtn.className == "fal fa-plus") {
        choicesNextElement.style.display = "block";
        choicesBtn.className = "fal fa-minus";
    } else {
        choicesNextElement.style.display = "none";
        choicesBtn.className = "fal fa-plus";
    }
}


/*choices section'da choices-item-header üçün accordion*/

function choicesHeaderAccordion(e) {
    choicesHeaderNextElement = e.nextElementSibling;
    choicesHeaderBtn = e.children[0].children[0];

    if (choicesHeaderBtn.className == "fal fa-plus") {
        choicesHeaderNextElement.style.display = "none";
        choicesHeaderBtn.className = "fal fa-minus";
    } else {
        choicesHeaderNextElement.style.display = "block";
        choicesHeaderBtn.className = "fal fa-plus";
    }

    e.preventDefault()
    console.log(choicesHeaderBtn)
}



// START - products section'da sort by və show dropdowns

sortingBtn = document.querySelectorAll('.product-sorting-btn')
sortingBtn.forEach(function (btn) {
    window.addEventListener('click', function (e) {
        if (btn.contains(e.target)) {
            sortingIcon = btn.children[1].children[0];
            if (sortingIcon.className == 'far fa-chevron-down') {
                sortingIcon.className = 'far fa-chevron-up'
                sortingList = btn.nextElementSibling;
                sortingList.style.display = 'block';
                btn.style.borderTopLeftRadius = '10px'
                btn.style.borderTopRightRadius = '10px'
                btn.style.borderBottomLeftRadius = '0px';
                btn.style.borderBottomRightRadius = '0px';
            } else {
                sortingList = btn.nextElementSibling;
                sortingList.style.display = 'none';
                btn.style.borderRadius = '30px'
                sortingIcon = btn.children[1].children[0];
                sortingIcon.className = 'far fa-chevron-down';
            }

        } else {
            sortingList = btn.nextElementSibling;
            sortingList.style.display = 'none';
            btn.style.borderRadius = '30px'
            sortingIcon = btn.children[1].children[0];
            sortingIcon.className = 'far fa-chevron-down';
        }
    })
})

// sortingSubList = document.querySelectorAll('.sub-list ul a');
// sortingSubList.forEach(function(list){
//     list.addEventListener('click',function(e){
//         sortingName = list.parentElement.parentElement.previousElementSibling.children[0];
//         listName = list.children[0];
//         sortingName.textContent=listName.textContent;
//         console.log(listName)
//         console.log(sortingName.textContent)
//         e.preventDefault();
//     })
// })

// END - products section'da sort by və show dropdowns