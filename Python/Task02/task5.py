n = int(input("Ededlerin sayi: "))
arr=[]
arrB=[]
arrK=[]
for i in range(n):
    eded = int(input(f'{i+1}. eded: '))
    arr.append(eded)

for eded in arr:
    if eded%2==0:
        if eded>=20:
            arrB.append(eded)
        else:
            arrK.append(eded)
print(f"Boyuk list: {arrB}")
print(f"Kicik list: {arrK}")

