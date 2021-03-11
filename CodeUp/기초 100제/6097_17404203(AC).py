import sys
input=sys.stdin.readline
h,w=map(int,input().split())
pan = [[0]*w for _ in range(h)]
n=int(input())
for _ in range(n):
  l,d,x,y=map(int,input().split())
  if d == 0:
    for i in range(l):
      pan[x-1][y+i-1]=1
  else :
    for i in range(l):
      pan[x+i-1][y-1]=1
    
for i in range(len(pan)):
  print(*pan[i])
  
# 설탕과자 뽑기 - 판 위에 막대(가로,세로) 올리면 올린부분 1로 바뀜

