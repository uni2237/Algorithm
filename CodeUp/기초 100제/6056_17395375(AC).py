import sys
input= sys.stdin.readline

a,b=map(int,input().split())
a=bool(a)
b=bool(b)

print((a and not b) or (not a and b))
# xor
