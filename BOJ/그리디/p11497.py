import sys
sys.stdin=open("Algorithm/input.txt","rt")
input = sys.stdin.readline

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    tree=list(map(int,input().split()))
    tree.sort()
    queue=deque()
    for _ in range(len(tree)//2):
        max1=tree.pop()
        max2=tree.pop()
        queue.appendleft(max1)  # 제일 큰 나무들을 가운데부터 양옆으로 붙임
        queue.append(max2)
    if tree:
        queue.appendleft(tree[0])
    #print(queue)
    diff=[]
    for i in range(len(queue)-1):
        a=queue[i]
        b=queue[i+1]
        diff.append(abs(a-b))
    diff.append(abs(queue[0]-queue[-1]))
    print(max(diff))



# 다른 사람 풀이

t = int(input())

for _ in range(t):
    n = int(input())
    heights = [int(x) for x in input().split()]
    heights.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(heights[i] - heights[i - 2]))

    print(max_level)
