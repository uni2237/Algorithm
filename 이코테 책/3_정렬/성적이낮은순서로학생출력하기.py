import sys
sys.stdin = open("input.txt","rt",encoding="UTF8")
input=sys.stdin.readline

n=int(input())
student=[]
for _ in range(n):
    key,value=input().split()
    student.append([key,int(value)])
'''
def setting(data):
    return data[1]

student = sorted(student, key=setting)
'''

for s in sorted(student,key=lambda student:student[1]):
    print(s[0],end=' ')

