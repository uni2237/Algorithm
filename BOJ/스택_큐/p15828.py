import sys
#sys.stdin=open("Algorithm/input.txt","rt")
input= sys.stdin.readline

from collections import deque
queue= deque()

n = int(input())
while True:
    num = int(input())
    
    if num==-1:
        break
    elif num==0:
        queue.popleft()
    elif len(queue)<n:
        queue.append(num)
if queue:
    print(*queue)
else:
    print("empty")