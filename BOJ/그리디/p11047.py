import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

from collections import deque
n,k=map(int,input().split())
money=deque()
for _ in range(n):
    money.appendleft(int(input()))

count=0

for m in money:
    if k==0: break
    count+=k//m
    k=k%m
    
print(count)
    