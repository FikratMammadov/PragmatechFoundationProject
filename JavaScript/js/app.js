btns=document.querySelectorAll('#btn');
// btn =document.querySelector('#btn');
// btns[0].addEventListener('click', function (){
//     console.log("Btn clicked");
// })

for(let i=0;i<btns.length;i++){
    btns[i].addEventListener('click', function (){
        console.log("Btn clicked");
    })
}
// console.log(btn)
