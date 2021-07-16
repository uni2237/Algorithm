import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(x, y, d):
    room[x][y]=2
    count=1
    while True:
        for i in range(4):
            nd=(d+3)%4
            nx,ny = x+dx[nd],y+dy[nd]
            d=nd
            if room[nx][ny]==0:
                room[nx][ny]=2
                count+=1
                x,y=nx,ny
                break
        else: 
            nd=(d+2)%4
            nx,ny = x+dx[nd],y+dy[nd]
            
            if room[nx][ny]==1:
                break
            else:
                x,y=nx,ny
    return count


print(solve(r, c, d))

# 북(0) 0-3-2-1
# 동(1) 1-0-3-2
# 남(2) 2-1-0-3
# 서(3) 3-2-1-0
# => (지금방향+3)%4 가 다음 왼쪽 방향!
# => (지금방향+2)%4 가 후진 방향!