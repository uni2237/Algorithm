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


########## 버전 1 #############
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


########## 버전 2 #############

def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<m and array[a][b]==0:
                queue.append([a,b])
                array[a][b] = array[x][y]+1
bfs()
day = 0
for i in array:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    day = max(day,max(i)) # 2차원 배열 속 가장 큰 값으로 day 갱신
print(day-1) # 1부터 시작했으니 -1 해준다.