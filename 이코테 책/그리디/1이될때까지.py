import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline
n,k=map(int,input().split())

count=1

while k**count <=n:
    count+=1
    
print(n-(k**(count-1))+(count-1))