# Öz Soyadınızı tərsdən yazdıran proqram yazın

surname="Mammadov"
inverse=""
i=len(surname)-1
while(i>=0):
    inverse+=surname[i]
    i-=1
print(inverse)