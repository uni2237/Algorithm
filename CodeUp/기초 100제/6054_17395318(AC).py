import sys
input= sys.stdin.readline

a,b=map(int,input().split())

print(bool(a) and bool(b))
# and 로 둘다 참일때만 True 출력
