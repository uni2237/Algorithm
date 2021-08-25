import sys
sys.stdin = open("input.txt","rt")
input=sys.stdin.readline

n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())),reverse=True)

for i in range(k):
    if b[i]>a[i]:
        a[i],b[i]=b[i],a[i]
print(sum(a))