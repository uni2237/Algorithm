import sys
sys.stdin = open("Algorithm/input.txt","rt")
input = sys.stdin.readline

import heapq

n = int(input())

heap=[]

for _ in range(n):
    num =int(input())
    if num==0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, num)
