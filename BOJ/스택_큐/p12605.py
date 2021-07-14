import sys
sys.stdin=open("Algorithm/input.txt","rt")
input = sys.stdin.readline

t = int(input())
for i in range(t):
    stack = list(input().split())
    print("Case #{}: ".format(i+1),end='')
    while len(stack)>0:
        print(stack.pop(),end=' ')
    print()