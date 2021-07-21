import sys
sys.stdin=open("Algorithm/input.txt","rt")
input = sys.stdin.readline
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())
arr = [ list(map(int, input().rstrip())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]  

queue = deque()
queue.append((0,0))
visited[0][0] = 0
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1:
                if not arr[nx][ny] :
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
print(visited[n-1][m-1])