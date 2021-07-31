import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

m,n =map(int,input().split())

array=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

from collections import deque
queue=deque()

for i in range(n):
    for j in range(m):
        if array[i][j]==1:
            queue.append((i,j)) # 처음부터 익어있던 토마토 -> 큐에 넣고 시작

day=-1
while queue: # 큐에 뭔가 남아있음 (첫 시작 or 추가로 익은 토마토들)
    day+=1 # 날짜 +1
    for _ in range(len(queue)): # 현재 익은 토마토 만큼 for문
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and array[nx][ny]==0:
                array[nx][ny]=array[x][y]+1 # 새로운 토마토가 익음.
                queue.append((nx,ny)) # 새로 익은 토마토 큐에 넣어줌.
    
for a in array:
    if 0 in a:
        print(-1) # 덜익은 토마토가 남아있으니 -1 출력
        break
else:
    print(day) # 모두 익었으니 총 day 출력