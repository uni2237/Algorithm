import sys
from heapq import heappop,heappush
#sys.stdin = open("BOJ/input.txt","rt")
input= sys.stdin.readline
#INF=sys.maxsize 
INF=int(1e9) # 이게 sys.maxsize 보다 빠름

m,n = map(int,input().split())

maze = [list(map(int,input().rstrip())) for _ in range(n)]
distance = [[INF] * m for _ in range(n)]
dx=[1,-1,0,0] 
dy=[0,0,-1,1] 


def dijkstra():
    q=[]
    heappush(q, (0, 0,0))
    distance[0][0]=0
    while q:
        room,x,y=heappop(q)
        if x == n-1 and y == m-1:
            print(room)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<=ny <m :
                nroom = room + maze[nx][ny]
                if distance[nx][ny] > nroom:
                    distance[nx][ny] = nroom
                    heappush(q, (nroom, nx,ny))
    
dijkstra()


    
