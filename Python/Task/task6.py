# Verilən cümlənin icərisində olan saitlərin sayını tapan proqram yazın

saitler = ["a","ı","o","u","e","ə","i","ö","ü"]
cumle="Salam gözəl oğlan"
say=0
for i in saitler:
    for j in cumle:
        if i==j:
            say+=1
print(say)

