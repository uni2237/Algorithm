import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

n=int(input())
pair=int(input())

array=[[0]*(n+1) for _ in range(n+1) ]


for _ in range(pair):
    a,b=map(int,input().split())
    array[a][b],array[b][a]=1,1

visited=[]

# dfs 방식
def dfs(start,array,visited):
    visited.append(start)
    for i in range(n+1):
        if array[start][i] and i not in visited:
            visited=dfs(i,array,visited)
    return visited
    
# bfs 방식
from collections import deque

def bfs(start,array):
    visited=[]
    queue=deque([start])
    visited.append(start)
    while queue:
        start=queue.popleft()
        for i in range(n+1):
            if array[start][i] and i not in visited:
                queue.append(i)
                visited.append(i)
    return len(visited)-1


print(len(dfs(1,array,visited))-1)
print(bfs(1,array))