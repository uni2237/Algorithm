import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline


n,m=map(int,input().split())
ice=[[int(x) for x in input().rstrip()] for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

count=0

def dfs(x,y):
    if (x<0 or x>=n) or (y<0 or y>=m):
        return False
    
    if ice[x][y]==0:
        ice[x][y]=1
        
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True # 연결된 칸들 다 돌때마다 True 반환

    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True: # True 나왔을때마다 한 덩어리씩임!
            count+=1
print(count)