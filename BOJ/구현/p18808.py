import sys 
sys.stdin=open("Algorithm/input.txt","rt")
input = sys.stdin.readline
import copy

# 90도 회전한 스티커 반환
def rotate(r,c,sticker):
    new_sticker=[ [sticker[r-j-1][i] for j in range(r)] for i in range(c) ]
    return c,r,new_sticker

# 스티커 붙일 수 있는지 True/False(=> 스티커랑 노트북 둘다 1일경우)
def check(x,y,r,c,sticker):
    
    for i in range(r):
        for j in range(c):
            if sticker[i][j]==0:
                continue
            else:
                if laptop[x+i][y+j]==1:
                    return False
    return True

# 노트북에 스티커 붙임 (노트북에 스티커 붙여진 칸마다 +1)
def attach(x,y,r,c,sticker):
    for i in range(r):
        for j in range(c):
            if sticker[i][j]==1:
                laptop[x+i][y+j]=1


n,m,k=map(int,input().split())
laptop=[[0]*m for _ in range(n)]

for _ in range(k):
    r,c=map(int,input().split())
    sticker=[list(map(int,input().split())) for _ in range(r)]
    
    rotate_count=0

    while rotate_count<4: # 회전은 최대 3번까지
        
        # 1. 노트북이랑 스티커 크기 비교 -> 맞을때 까지 회전해서 비교
        if r>n or c>m:
            r,c,sticker=rotate(r,c,sticker)
            rotate_count+=1
            continue 
        
        flag=0
        # 2. 스티커 붙일 시작점 범위에서, 스티커 붙일 수 있는 지 확인
        for i in range(n-r+1): # 스티커 크기 만큼 빼준 범위
            for j in range(m-c+1):
                if not check(i,j,r,c,sticker) : # 스티커 못 붙이면?
                    continue
                else: # 스티커 붙이면?
                    attach(i,j,r,c,sticker)
                    flag=1
                    break
            if flag: break
        if flag: break
        else:
            r,c,sticker=rotate(r,c,sticker)
            rotate_count+=1
result=0
for i in range(n):
    for j in range(m):
        if laptop[i][j]==1:
            result +=1
print(result)



