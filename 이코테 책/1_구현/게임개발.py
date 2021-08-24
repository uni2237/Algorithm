import sys
from typing import MappingView
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

n,m=map(int,input().split())
x,y,d=map(int,input().split())

map=list(list(map(int,input().split())) for _ in range(n))
visit=[[0]*m for _ in range(n)]

# 북서남동
dx=[-1,0,1,0]
dy=[0,-1,0,1]

rotate_count=0
visit[x][y]=1
count=1

while True:
    
    d = d-1 if (d!=0) else 3
    nx,ny=x+dx[d],y+dy[d]
    
    # 회전한 이후, 정면에 안 가본 칸 있을 때
    if map[nx][ny]==0 and visit[nx][ny]==0 :
        visit[nx][ny]=1
        rotate_count=0
        count+=1
        x,y=nx,ny
        continue
    else: # 회전한 이후, 가보지않은 칸이 없거나 바다인경우
        rotate_count+=1

    # 네 방향 모두 못감
    if rotate_count==4 :
        
        # 뒤로 이동 시 
        behind=(d+2)%4
        nx,ny=x+dx[behind],y+dy[behind]
        # behind 안쓰고 바로 nx,ny= x-dx[d], y-dy[d] 이렇게 해도 됨.
        
        # 뒤로 갈수있음
        if map[nx][ny]==0:
            x,y=nx,ny # 이미 방문한곳이므로 x,y만 변경해주고, visit과 count는 변경 팔요 x 
        # 뒤가 바다라 못감  
        else:
            break
        rotate_count=0
            
    
    

print(count)