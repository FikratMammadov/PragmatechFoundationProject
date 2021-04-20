n=int(input("Girilecek Eded Sayi: "))
arr=[]
i=0
sum=0
while(i<n):
    eded  = input(f'{i+1}. eded: ')
    i+=1
    arr.append(eded)

for eded in arr:
    if(eded.isdecimal()):
        sum+=int(eded)
    else:
        print("Problem var")
        break
    
    if(arr.index(eded)==len(arr)-1):
        print(sum)