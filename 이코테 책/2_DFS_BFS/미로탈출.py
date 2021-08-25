import sys
sys.stdin = open("input.txt","rt")
input=sys.stdin.readline

n,m=map(int,input().split())

maze=[ [int(x) for x in input().rstrip()] for _ in range(n) ]

from collections import deque
que=deque()


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    que.append((x,y))

    while que:
        x,y=que.popleft()
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif maze[nx][ny]==0:
                continue
            elif maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                que.append((nx,ny))
    return maze[n-1][m-1]
print(bfs(0,0))