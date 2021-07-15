import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global count
    if room[x][y] == 0:
        room[x][y] = 2
        count += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if room[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if room[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

count = 0
clean(r, c, d)
print(count)

# 북(0) 0-3-2-1
# 동(1) 1-0-3-2
# 남(2) 2-1-0-3
# 서(3) 3-2-1-0
# => (지금방향+3)%4 가 다음 왼쪽 방향!