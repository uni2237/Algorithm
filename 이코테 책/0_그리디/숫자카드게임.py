import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

n,m=map(int,input().split())
a=min(list(map(int,input().split())))
for _ in range(n-1):
    new=min(list(map(int,input().split())))
    a = (a > new) and a or new  # 파이썬 삼항연산자 -> ? 대신 and, : 대신 or 사용
                                # 혹은 a = a if (a>new) else new
    # a = max(a,new)  이렇게 해도 됨.
print(a)