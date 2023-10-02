import sys
sys.stdin=open("Algorithm/input.txt")
input=sys.stdin.readline

string=input().rstrip()
arr=[]
for i in range(len(string)):
    arr.append(string[i:])
for i in sorted(arr):
    print(i)