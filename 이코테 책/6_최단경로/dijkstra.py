import heapq
import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
INF=int(1e9) # 무한을 의미하는 10억

n,m=map(int,input().split()) # 노드 수, 간선 수
start=int(input()) # 시작 노드 번호

graph=[[] for _ in range(n+1)] # 인접리스트
distance=[INF]*(n+1) # 최단거리 테이블 모두 무한으로 초기화

# 간선 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) # a에서 b로 가는 거리가 c

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # 큐에 (거리,노드번호) 순으로 넣음. -> 거리를 기준으로 정렬되도록!
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q)

        if distance[now]<dist: # 최단거리테이블 속 거리가 더 짧으면 넘김~!
            continue

        for neighbor in graph[now]: # 현재노드(now)의 인접노드들(neighbor) 검사
            cost=dist+neighbor[1] 
            
            # 현재노드 거쳐서, 인접노드로 이동하는 거리가 더 짧다면? 
            if cost<distance[neighbor[0]]: 
                distance[neighbor[0]]=cost # 최단거리테이블 갱신!
                heapq.heappush(q,(cost,neighbor[0])) 

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])

''' input 
6 11
1 
1 2 2 
1 3 5
1 4 1 
2 3 3 
2 4 2
3 2 3
3 6 5 
4 3 3 
4 5 1 
5 3 1 
5 6 2
'''