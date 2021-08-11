import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline


n=int(input())
store=list(map(int,input().split()))

m=int(input())
li=list(map(int,input().split()))



''' set 이용
n=int(input())
store=set(map(int,input().split()))

m=int(input())
li=list(map(int,input().split()))

for i in li:
    if i in store:
        print("yes",end=' ')
    else:
        print("no",end=' ')
'''

    