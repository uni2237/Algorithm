# ================= BFS 동작 과정 (큐 이용) ==================

#  1. 시작 노드를 큐에 삽입하고 방문 처리
#  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
#  3. 2 번의 과정을 더 이상 수행할 수 없을 때까지 반복

#                [1]ㅡㅡㅡ[2]
#               /  \        \
#              /    \        \
#             [3]    \       [7]     
#             | \     \     / ㅣ    
#             |  \     \   /  ㅣ     
#            [4]ㅡ[5]   [8]   [6]
#
#        bfs 결과 : 1-2-3-8-7-4-5-6


graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True # 현재 노드 방문처리
    
    while queue:
        v=queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]: # 현재 노드의 인접노드들 중 방문안한 노드 발견시 dfs재귀적 호출
                queue.append(i)
                visited[i]=True

bfs(graph,1,visited)  # 1 2 3 8 7 4 5 6

