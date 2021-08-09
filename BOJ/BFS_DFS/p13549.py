import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

queue = deque()
vis = [-1] * 200001

queue.append(n)
vis[n] = 0

while queue:
    x = queue.popleft()
    if x == k:
        print(vis[x])
        sys.exit()
    # 순간이동
    if 2*x <= 200000 and vis[2*x] == -1:
        vis[2*x] = vis[x]
        # appendleft로 순간이동 시 큐의 앞에 넣어 먼저 접근 가능하도록 함
        queue.appendleft(2*x)

    # x-1 
    if x - 1 >= 0 and vis[x - 1] == -1:
        vis[x - 1] = vis[x] + 1
        queue.append(x - 1)
    # x+1 
    if x + 1 <= 200000 and vis[x + 1] == -1:
        vis[x + 1] = vis[x] + 1
        queue.append(x + 1)
