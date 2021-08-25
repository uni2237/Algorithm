import sys
sys.stdin = open("input.txt","rt")
input=sys.stdin.readline

n=int(input())

a=[]
for _ in range(n):
    a.append(int(input()))

print(*sorted(a,reverse=True))