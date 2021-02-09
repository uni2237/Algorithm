# 간단한 다익스트라 알고리즘 

import sys
input= sys.stdin.readline
INF=int(1e9) # 무한대(10억)

n,m = map(int,input().split()) # 노드 수, 간선 수

start = int(input()) # 시작 노드
graph= [ [] for i in range(n+1)] # 각 노드마다 연결된 노드들의 정보 저장
visited = [False] * (n+1) # 방문 체크 리스트
distance = [INF] * (n+1) # 최단 거리 테이블 무한대로 초기화

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append( (b,c) ) # a 에서 b로 가는 비용이 c 


# 방문 안 한 노드 중, 최단 거리 가장 짧은 노드 번호 얻기 위한 함수!!!
def get_smallest_node():
    min_value = INF
    idx = 0 # 최단 거리 가장 짧은 노드 (인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i] # 최단 거리 가장 짧은 거 나올 떄 까지 min_value 계속 초기화
            idx = i # 최단 거리 가장 짧은 노드의 번호를 idx로 저장
    return idx

def dijkstra(start):

    # 시작 노드 
    distance[start]=0
    visited[start]=True 

    #시작 노드랑 연결된 노드들 최단거리 테이블 초기화
    for n in graph[start]:
        distance[n[0]] = n[1] 
    
    # 시작 노드 제외한 n-1개의 노드들 중
    for i in range(n-1):
        now = get_smallest_node() # 최단거리 가장 짧은 노드 now로 저장하고
        visited[now] = True       # 방문 True로 변경, (이게 현재 노드)

        # 현재 노드랑 연결된 노드들 중 (연결된 노드 : n) 
        for n in graph[now]:      
            cost = distance[now] + n[1] # cost : 현재 노드 거쳐서 n 까지 가는 거리
            if cost < distance[n[0]]:   # 지금까지 최단거리 테이블에 저장된 n까지의 거리가, 현재 노드 거쳐서 새로 계산한 cost 보다 크다면? 
                distance[n[0]] = cost   # 최단거리 테이블 값 거쳐가는 걸로 변경!!

# 다익스트라 수행
dijkstra(start)

# 노드마다의 최단거리 출력
for i in range(1, n+1):
    if distance[i] = INF: # 중간에 연결이 끊겨 도달 못한 노드
        print("INFINITY")
    else: 
        print(distance[i])