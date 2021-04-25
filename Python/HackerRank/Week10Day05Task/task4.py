# Write a function
# https://www.hackerrank.com/challenges/write-a-function/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def is_leap(_year):
    if(_year%100==0 and _year%400==0):
        return True
    elif _year%4==0 and _year%100!=0:
         return True
    else:
        return False

year = int(input())
print(is_leap(year))