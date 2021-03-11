import sys
input= sys.stdin.readline

a,b=map(int,input().split())
a=bool(a)
b=bool(b)

print((a == b)) # 참/거짓 같을 때만 True 출력
