import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

n,m=map(int,input().split())
maze=[list(map(int,list(input().rstrip()))) for _ in range(n)]
print(maze)

visited= [[-1]*m for _ in range(n)]

visited[0][0]=1
from collections import deque
queue=deque()
queue.append((0,0))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1: # 방문 x
            if maze[nx][ny]==1: # maze에서 1이라면(이동가능)
                queue.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1 # 방문 비용 +1
print(visited[n-1][m-1])
