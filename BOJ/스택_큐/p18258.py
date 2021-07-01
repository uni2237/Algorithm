import sys
sys.stdin = open("Algorithm/input.txt","rt")
input=sys.stdin.readline

from collections import deque
queue=deque()

n= int(input())
size=0
for _ in range(n):
    array=input().split()
    word=array[0]

    if word=='push':
        queue.append(int(array[1]))
        size+=1
    elif word=='pop':
        if size==0:
            print(-1)
        else:
            print(queue.popleft())
            size-=1
    elif word=='size':
        print(size)
    elif word=='empty':
        if size==0:
            print(1)
        else:
            print(0)
    elif word=='front':
        if size==0:
            print(-1)
        else:
            print(queue[0])
    else:
        if size==0:
            print(-1)
        else:
            print(queue[-1])
