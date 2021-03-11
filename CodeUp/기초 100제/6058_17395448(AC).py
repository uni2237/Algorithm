import sys
input= sys.stdin.readline

a,b=map(int,input().split())
a=bool(a)
b=bool(b)

print((not a and not b)) # 둘다 거짓이면 true 출력 
