import sys
input=sys.stdin.readline
l=[0 for i in range(23)]
a= int(input())
num = list(map(int, input().split()))
for i in num:
  l[i-1]+=1
  
print(*l)
# 23개의 숫자들중 어떤 것이 몇번 입력되었는지
