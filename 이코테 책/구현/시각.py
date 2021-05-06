import sys
sys.stdin = open("Algorithm\input.txt","rt")
input= sys.stdin.readline

count=0
n=int(input())

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)