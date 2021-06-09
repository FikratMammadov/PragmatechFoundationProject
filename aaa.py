num = int(input('4 reqemli eded daxil edin: '))
for i in str(num):
    if num % int(i)==0:
        if str(num)[len(str(num))-1]:
            print('Yes')
    else:
        print('No')
        break;
