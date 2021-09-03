import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
INF=int(1e9)

# 노드 수, 간선 수
n,m=int(input()),int(input())


graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기자신으로 가는 거리 = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# a에서 b로 가는 거리 =c
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

# a -> b 의 거리를 a->b 와 a->k->b 중 더 짧은 것으로 갱신
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=' ')
        else:
            print(graph[a][b],end=' ')
    print()

''' input
4
7
1 2 4 
1 4 6 
2 1 3 
2 3 7 
3 1 5 
3 4 4 
4 3 2
'''