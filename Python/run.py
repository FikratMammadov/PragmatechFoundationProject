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

n=int(input())

if n%2==1:
    print("Weird")
else:
    if n in range(2,5):
        print("Not Weird")
    if n in range(6,20):
        print("Weird")
    if n>20:
        print("Not Weird")
    