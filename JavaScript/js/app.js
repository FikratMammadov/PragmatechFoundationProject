// a=2;

// function topla(){
//     let a=3;
//     console.log(a);
// }
// topla();
// console.log(a)


// a=prompt("Birinci ededi daxil edin: ");
// console.log(String(a*1)=="NaN");



// 1. num1 deyisenini elan et // let num1;
// 2. num2 deyisenini elan et // let num2;
// 3. sum deyisenini elan et // let sum;
// 4. birinci ededi daxil et // prompt()
// 5. daxil edilen ededi num1 e menimset // num1=promt()
// 6. ikinci ededi daxil et // prompt()
// 7. daxil edilen ededi num2 e menimset // num2=promt()
// 8. num1 deyiseninin tipini oyren //type of
// 9 num1*1 emeliyatinin neticesini yoxla // console.log(num1*1);
// 10. num1 ve num2 nin eded oldugunu yoxla // if


// Week 05 Ders 02
// function Teacher(_ad,_soyad,_yas){
//     this.ad=_ad;
//     this.soyad=_soyad;
//     this.yas=_yas;
//     this.melumatGoster=function(){
//         console.log(this.ad+" "+this.soyad+" "+this.yas);
//     }
// }

// let muellim1=new Teacher("Samir","Karimov",40);
// muellim1.melumatGoster();


// class Person {
//     constructor(_name){
//         this.#name=_name;
//     }

//     Introduce(){
//         console.log(`My name is ${this.#name}`);
//     }

// }

 
// let p1=new Person("Firkat");

// console.log(p1.Introduce());

arr=[4,5,2,2,5,3,1,7];
let min=arr[0]

for(let i=1;i<arr.length;i++){
    for(let j=0;j<arr.length;j++){
        if(arr[i]<min){
        min=arr[i]
    }
    }
    
}
console.log(min)



