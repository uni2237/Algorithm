import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

n,m=map(int,input().split())
array=[[int(i) for i in input().rstrip()] for _ in range(n)]

visited=[[-1]*m for _ in range(n)]
print(array)
print(visited)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

from collections import deque
queue=deque()
queue.append((0,0))
visited[0][0]=0

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny]==-1: # 아직 방문 x
                if array[nx][ny]==1: # 벽일 때
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx,ny)) # 큐 뒤에 추가
                else: # 빈방일때
                    visited[nx][ny]=visited[x][y]
                    queue.appendleft((nx,ny)) # 큐 앞에 추가
print(visited[n-1][m-1])

