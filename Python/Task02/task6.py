arr=[5,6,5,17,23,32,23]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j:
            if arr[i]==arr[j]:
                break
            else:
                if(j==len(arr)-1):
                    print(arr[i],end=" ")
            