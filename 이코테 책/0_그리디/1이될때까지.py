import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline
n,k=map(int,input().split())

count=1

while k**count <=n:
    count+=1
    
print(n-(k**(count-1))+(count-1))

# 나누기 부터 계속 하는게 그리디 ! 나는 제곱으로 쉽게 구했음.