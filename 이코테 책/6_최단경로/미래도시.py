import sys
import heapq
sys.stdin=open("input.txt","rt")
input = sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]


for _ in range(2,m+2):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j]=0

x,k=map(int,input().split())

# 1->k->x 방문

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print(-1)
else:
    print(distance)


