import sys
sys.stdin = open("Algorithm\input.txt","rt")
input=sys.stdin.readline

n,k = map(int,input().split())
a= list(map(int,input().split()))
b= list(map(int,input().split()))

a.sort()
b.sort(reverse=True)


for i in range(k):
    if b[i]>a[i] :
        a[i],b[i]=b[i],a[i] # swap
    else:
        break

print(sum(a))
