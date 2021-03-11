import sys
input=sys.stdin.readline
a= int(input())

num = list(map(int, input().split()))

# 입력받은 수들 거꾸로 출력
for i in range(1, len(num)+1): # 범위 오름차순,인덱스를 음수로 출력
  print(num[-i],end=" ")  
  
#for i in range(a-1,-1,-1): # 범위 내림차순 출력
#  print(num[i],end=" ") 
