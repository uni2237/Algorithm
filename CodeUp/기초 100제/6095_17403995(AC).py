import sys
input=sys.stdin.readline
num= int(input())
badook = [[0]*19 for _ in range(19)]

for _ in range(num):
  x,y=map(int,input().split())
  badook[x-1][y-1]=1

for i in range(len(badook)):
  print(*badook[i])
