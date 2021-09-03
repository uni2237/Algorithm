import sys
import heapq
sys.stdin=open("input.txt","rt")
input = sys.stdin.readline
INF=int(1e9)

n,m,c=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def solution(c):
    q=[]
    distance[c]=0
    heapq.heappush(q,(0,c))

    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for neighbor in graph[now]:
            cost=neighbor[1]+ dist

            if cost<distance[neighbor[0]]:
                distance[neighbor[0]]=cost
                heapq.heappush(q,(cost,neighbor[0]))
    count=0
    time=0
    for d in distance:
        if d!=INF:
            count+=1
            time=max(time,d)
    print(count-1,time)
solution(c)

