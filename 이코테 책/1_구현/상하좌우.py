import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

n=int(input())
input_com=input().split()
x,y=1,1
print(n)
print(input_com)

#LRUD : 좌우상하
dx=[0,0,-1,1]
dy=[-1,1,0,0]
command=['L','R','U','D']

for c in input_com:
    for i in range(len(command)):
        if c == command[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x,y=nx,ny

print(x,y)

