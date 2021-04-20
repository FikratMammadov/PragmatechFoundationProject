n = int(input("Listin elementlerinin sayi: "))
arr=[]
say =0
for i in range(n):
    elem = input(f"{i+1}. element: ")
    arr.append(elem)

for elem in arr:
    if elem == elem[::-1]:
        say+=1
print(say)
