import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

n, m = map(int, input().split())

graph =[ [int(x) for x in input().rstrip()] for _ in range(n)]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return 0

    if graph[x][y]==0:
        graph[x][y]=1
        #상하좌우 
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return 1
    return 0

count=0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==1:
            count+=1
print(count)
            

