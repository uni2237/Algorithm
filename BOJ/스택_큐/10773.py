import sys
sys.stdin=open("Algorithm/input.txt","rt")
input = sys.stdin.readline

k=int(input())
stack=[]

for _ in range(k):
    num=int(input())

    if num==0:
        stack.pop(-1)

    else:
        stack.append(num)
print(sum(stack))
