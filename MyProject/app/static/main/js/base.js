// search box 
let searchBtn = document.querySelector('.header-menubar-account .fa-search');
let searchBox = document.querySelector('#search')
let exitBtn = document.querySelector('.serach-exit i')
searchBtn.addEventListener('click', function () {
    searchBox.className = 'show'
})

exitBtn.addEventListener('click', function () {
    searchBox.className = 'hide'
})

// cart button
let cartBtn = document.querySelector('.fa-shopping-bag')
let shoppingCart = document.querySelector('.shopping-cart')

cartBtn.addEventListener('mouseover', function () {
    shoppingCart.className = 'shopping-cart show'
});
cartBtn.addEventListener('mouseout', function () {
    shoppingCart.className = 'shopping-cart hide'
});
// console.log(shoppingCart.children.contains(e.target))
shoppingCart.addEventListener('mouseover', function () {
    shoppingCart.className = 'shopping-cart show'
});
shoppingCart.addEventListener('mouseout', function () {
    shoppingCart.className = 'shopping-cart hide'
});
let cart, cartFooter
let addBtn = document.querySelectorAll('.cake-item-btn.add-cart')
let cartItemNumber = 0
let total
products = []
function addCartItem() {
    addBtn.forEach(function (btn) {
        btn.addEventListener('click', function () {
            let productImgAll = btn.parentElement.previousElementSibling.children[0].children[0].children[0].src
            let indexImg = productImgAll.indexOf('img') + 3
            let productImg = productImgAll.slice(indexImg)
            let price = parseFloat(btn.parentElement.children[1].textContent.slice(1))
            let title = btn.parentElement.children[0].textContent
            let product = {
                num: 1,
                img: productImg,
                price: price,
                title: title
            }

            // console.log(product)
            // if (products.length == 0) {
            //     console.log('ferqli')
            //     products.push(product)
            //     console.log(products)
            //     cartItem = document.createElement('div')
            // } else {
            //     for (i = 0; i < products.length; i++) {
            //         if (products[i].title == product.title) {
            //             console.log('eyni')
            //             products[i].num++;
            //             product.num = products[i].num
            //             console.log(products[i].num)
            //             if (i == products.length - 1 && products[i].title != product.title) {
            //                 console.log('ferqli')
            //                 products.push(product)
            //                 console.log(products)
            //                 cartItem = document.createElement('div')
            //             }
            //         }


            //     }
                 
            // }



            cartItem = document.createElement('div')
            cartItem.className = 'cart-item'
            cartItem.innerHTML = `
        <div class="cart-item-delete">
        <i class="fal fa-times"></i>
    </div>
    <div class="cart-item-img">
        <img src="../static/main/img${product.img}" alt="">
    </div>
    <div class="cart-item-desc">
        <div class="card-item-title">
            ${product.title}
        </div>
        <div class="card-item-price">
            $<span class="price">${product.price}.00</span> x <span class="piece">${product.num}</span>
        </div>
    </div>
        `
            // show cart item
            showCartItem()

            // get total price
            total = 0
            cartItemTotalPrice()

            // show cart footer when add to cart
            document.querySelector('.cart-footer').className = 'cart-footer show'

            // remove item
            removeCartItem()

            // set total price 
            cartTotalPrice = document.querySelector('.cart-total .total-price')
            cartTotalPrice.textContent = total

            // set cart item number
            cartItemNumber++;

            // get cart shoppingValue
            shoppingValue = document.querySelector('.shopping-value')

            // set cart item number
            shoppingValue.textContent = cartItemNumber


        })

    })
}

function showCartItem() {
    // select cart
    cart = document.querySelector('.shopping-cart')
    cartItems = document.querySelector('.cart-items')
    cartFooter = document.querySelector('.cart-footer')
    cartItems.appendChild(cartItem)
}

function cartItemTotalPrice() {
    cartItemPrice = document.querySelectorAll('.card-item-price .price')
    cartItemPrice.forEach(function (price) {
        total += parseFloat(price.textContent)
    })
}

function removeCartItem() {
    cartItems = document.querySelector('.cart-items')
    cartRemoveBtn = document.querySelectorAll('.cart-item-delete i')
    cartRemoveBtn.forEach(function (removeBtn) {
        removeBtn.addEventListener('click', function () {
            thisItem = removeBtn.parentElement.parentElement
            cartItems.removeChild(thisItem)

            if (cartItems.children.length == 0) {
                document.querySelector('.cart-footer').className = 'cart-footer hide'
            }

            thisPrice = removeBtn.parentElement.nextElementSibling.nextElementSibling.children[1].children[0].textContent
            total -= parseFloat(thisPrice)
            console.log(total)
            cartTotalPrice = document.querySelector('.cart-total .total-price')
            cartTotalPrice.textContent = total

            // set cart item number
            cartItemNumber--;

            // get cart shoppingValue
            shoppingValue = document.querySelector('.shopping-value')

            // set cart item number
            shoppingValue.textContent = cartItemNumber

        })
    });

}



// call addCartItem function
addCartItem()
// removeCartItem()




// shopping cart delete item





