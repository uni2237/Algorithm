import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

n,m,v=map(int,input().split())
array=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    array[a][b],array[b][a]=1,1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[]
def dfs(v,array,visited):
    visited.append(v)
    for i in range(n+1):
        if array[v][i]==1 and i not in visited:
            visited=dfs(i,array,visited)
    return visited


from collections import deque
def bfs(v,array):
    queue=deque([v])
    visited=[v]

    while queue:
        v=queue.popleft()
        for i in range(n+1):
            if array[v][i]==1 and i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(*dfs(v,array,visited))
print(*bfs(v,array))


