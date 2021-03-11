import sys
input= sys.stdin.readline

a=int(input())
for i in range(1,a+1):
  if i%10 not in (3,6,9):
    print(i, end=' ')
  else:
    print('X',end=' ')

# 1~29까지 3,6,9 게임 
