# sum=0
# for i in range(100):
#     if(i%2==1):
#         print(i)
#         sum=sum+i

# print(sum)

# cumle='Javascript ne vaxtdan proqramlasdirma dili olub?'
 
# for i in cumle:
#     if i==" " or i=="?":
#         i = ""
# print(cumle)
# print(len(cumle))

# ayri=cumle.split(" ")
# print(ayri)


# sentence = 'Javascript ne vaxtdan proqramlasdirma dili olub?'
# symbols="!/,.#$? "
# for txt in sentence:
#     for symbol in symbols:
#         if txt==symbol:
#             sentence=sentence.replace(txt,"")
# print(len(sentence))

# n=int(input())

# if n%2==1:
#     print("Weird")
# else:
#     if n in range(2,5):
#         print("Not Weird")
#     if n in range(6,21):
#         print("Weird")
#     if n>20:
#         print("Not Weird")

# num = 45342
# sum=0
# while num>0:
#     qaliq = num%10 
#     num = num//10 
#     sum+=qaliq 
# print(sum)

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

# x='Hello world'
# y=200
# # print(f"a{x.center(20,'-')}a")
# print(type(isinstance(y,int)))

# a = "this is a string"

# def split_and_join(chr):
#     myList = a.split()
#     print(chr.join(myList)) 
    
# split_and_join('-')

# a=3
# b=5

# print(a+b)
# print(a-b)
# print(a*b)