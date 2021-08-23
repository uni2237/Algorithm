import sys
sys.stdin=open("input.txt","rt")
input = sys.stdin.readline

n,m,k=map(int,input().split())
arr=sorted(list(map(int,input().split())))

max=arr[-1]
max2=arr[-2]

answer=(max*k+max2)*m//(k+1) + m%(k+1)*max
print(answer)

