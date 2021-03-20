import sys
input = sys.stdin.readline

t = int(input())
a=[]
b=[]

for _ in range(t):
    a.append(input().rstrip())
result=""
for i in range(len(a[0])):
    s=set()
    for j in range(t):
        s.add(a[j][i])
    if len(s)==1:
    	result= result+a[0][i]
    else:
        result=result+"?"
print(result) 

# 중복 체크를 해주는 set 을 이용!!
