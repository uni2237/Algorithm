import sys
input=sys.stdin.readline

badook = [list(map(int,input().split())) for _ in range(19)]
num= int(input())

for _ in range(num):
  x,y=map(int,input().split())
  for i in range(len(badook)):
    if badook[x-1][i]==1:
      badook[x-1][i]=0
    else:
      badook[x-1][i]=1
    if badook[i][y-1]==1:
      badook[i][y-1]=0
    else:
      badook[i][y-1]=1
    
    
for i in range(len(badook)):
  print(*badook[i])
  
# 2차원 공간 바둑판 주어지는 좌표들 기준으로 십자뒤집기(가로,세로 순) 
