# Lists
# https://www.hackerrank.com/challenges/python-lists/problem

lst=[]
n=int(input())
for i in range(n):
    cmd=input().split()
    if cmd[0]=='insert':
        lst.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=='print':
        print(lst)
    elif cmd[0]=='remove':
        lst.remove(int(cmd[1]))
    elif cmd[0]=='append':
        lst.append(int(cmd[1]))
    elif cmd[0]=='sort':
        lst.sort()
    elif cmd[0]=='pop':
        lst.pop()
    else:
        lst.reverse()