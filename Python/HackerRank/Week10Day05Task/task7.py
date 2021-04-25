# Find the Runner-Up Score! 
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
A=map(int,input().split())   
A=list(A)
A.sort()
max = A[0]
for num in A:   
    if num>max:
        temp = max
        max=num
     
print(temp)
    