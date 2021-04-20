# Verilən cümlənin icərisində olan saitlərin sayını tapan proqram yazın

saitler = ["a","ı","o","u","e","ə","i","ö","ü"]
cumle="Salam Mehdi necesen"
cumle2=cumle.lower()
say=0
for i in cumle2:
    for j in saitler:
        if i==j:
            say+=1
print(say)

