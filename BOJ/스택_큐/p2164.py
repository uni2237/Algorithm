import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

n = int(input())

from collections import deque
queue=deque()

for i in range(n):
    queue.append(i+1)

while len(queue)>1:
    queue.popleft()
    top = queue.popleft()
    queue.append(top)

print(*queue)