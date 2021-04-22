# 'Javascript ne vaxtdan proqramlasdirma dili olub?' cumlesinin herf sayini tapin

sentence='Javascript ne vaxtdan proqramlasdirma dili olub?'
sentenceList=list(sentence)

i=0
while i<len(sentenceList):
    if(sentenceList[i]==" "or sentenceList[i]=="?"):
        sentenceList.remove(sentenceList[i])
    i+=1
print(len(sentenceList))
