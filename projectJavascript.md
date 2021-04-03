## home-slider section'da slider qurulmasinin ardıcıllığı
1. slider content içindəki tagları homeSliderHeader, homeSliderDescription, homeSliderPrice, homeSliderBtn dəyişənləri içinə mənimsədildi.
2. butonlar homeSliderBtnLeft və homeSliderBtnRight dəyişənlərinə mənimsədildi.
3. Hər slide-a aid məlumatlar homeSliderContents arrayına mənimsədildi.
4. İlk başda görünən slide-ın indexine 0 dedik. // let index = 0
5. homeSliderBtnLeft və homeSliderBtnRight butonlarına click event verildi. // addEventListener
6. homeSliderBtnLeft click olunanda index-i 1 vahid azaldırıq. // index--
7. homeSliderBtnRight click olunanda index-i 1 vahid artırırq. // index++
8. click olunanda index 0 dan kicik olanda slide olmadığı üçün onu ən axrıncı index-ə yəni, homeSliderContents.length-1 i mənimsədirik. // if(i<0){index=homeSliderContents.length-1} 
9. clickk olunanda index homeSliderContents.length-1 den boyuk olanda slide olmadığı üçün onu birinci index'e 0-ı mənimsədirik. // if (index > homeSliderContents.length - 1){index = 0;}
10. click olunanda bgImage'i və content içindəkiləri dəyişmək üçün setHomeSliderContent() funksiyası yaradıldı.
11. və bu funksiyanı eventlər içərində çağırırıq
12. bu funksiya da event olunanda hansı indexə uyğundusa müəyyən dəyişikliklər edir.