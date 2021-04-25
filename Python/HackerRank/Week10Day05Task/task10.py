# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem 
n= int(input())
students = []
scores=[]
for i in range(n):
    name = input()
    score = float(input())
    students.append([name,score])
students.sort()
for student in students:
    scores.append(student[1])
scores.sort()
scores.reverse()
minScore=scores[0]
for score in scores:
    if score<minScore:
        temp = minScore
        minScore = score

for student in students:
    if student[1]==temp:
        print(student[0])
