import sys
sys.stdin = open("Algorithm/input.txt","rt")
input = sys.stdin.readline

t = int(input())

for i in range(t):
    dict={}
    n = int(input())
    for j in range(n):
        name, clothes= input().split()
        if clothes not in dict:
            dict[clothes]= 1
        else:
            dict[clothes]+=1
    sum=1
    for value in dict.values():
        sum*=(value+1)
    print(sum-1)

