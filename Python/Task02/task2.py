numOfList1 = int(input("1-ci listdeki ededlerin sayi: "))
list_1=[]
for i in range(numOfList1):
    eded = int(input(f"{i+1}. eded: "))
    list_1.append(eded)
print("****************")
numOfList2 = int(input("2-ci listdeki ededlerin sayi: "))
list_2=[]
for i in range(numOfList2):
    eded = int(input(f"{i+1}. eded: "))
    list_2.append(eded)

for i in list_1:
    for j in list_2:
        if i==j:
            print("True")
            break

        if(list_1.index(i)==len(list_1)-1 and list_2.index(j)==len(list_2)-1 and i!=j):
            print("False")
            
