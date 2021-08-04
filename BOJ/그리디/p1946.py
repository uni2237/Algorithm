import sys
sys.stdin=open("Algorithm/input.txt")
input=sys.stdin.readline

t= int(input())
for _ in range(t):
    all=[]
    n=int(input())
    for _ in range(n):
        
        all.append(list(map(int,input().split())))
        all.sort()
    std = all[0][1]
    count=n
    for i in range(1,len(all)):
        if all[i][1]>std:
            count-=1
            continue
        else:
            std=all[i][1]
    print(count)

