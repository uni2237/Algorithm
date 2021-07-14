import sys
sys.stdin = open("Algorithm/input.txt","rt")
input = sys.stdin.readline

n,m=map(int,input().split())

dict={}
for _ in range(n):
    url,pw=map(str, input().split())
    dict[url]=pw
for _ in range(m):
    key=input().rstrip()
    
    print(dict[key])