import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

stack=[]
n= int(input())
size=0
for _ in range(n):
    array=list(input().split())
    
    word=array[0]

    if word=='push':
        stack.append(int(array[1]))
        size+=1
    elif word=='pop':
        if size==0:
            print(-1)
        else:
            print(stack.pop(-1))
            size-=1
    elif word=='size':
        print(size)
    elif word=='empty':
        if size==0:
            print(1)
        else:
            print(0)
    else:
        if size==0:
            print(-1)
        else:
            print(stack[-1])
