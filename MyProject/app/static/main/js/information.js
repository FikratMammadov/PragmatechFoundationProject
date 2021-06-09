showSummary = document.querySelector('#information .order-summary')
orderSummaryBtn = document.querySelector('#information .order-summary .order-summary-btn')
selectedProduct = document.querySelector('#information #selected-product.clicked')


showSummary.addEventListener('click',function(){
    if (selectedProduct.style.display=='none'){
        selectedProduct.style.display='block'
        orderSummaryBtn.innerHTML = `<i class="fal fa-shopping-cart"></i> Hide order summary  <i class="fal fa-chevron-up"></i>`
    }else{
        selectedProduct.style.display='none'
        orderSummaryBtn.innerHTML = `<i class="fal fa-shopping-cart"></i> Show order summary  <i class="fal fa-chevron-down"></i>`
    }
    
})