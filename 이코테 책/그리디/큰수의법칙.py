import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
num = list(map(int, input().split()))
num.sort()

max=num[-1]
min=num[-2]

count = m / (k+1)
plus = m  - count*(k+1)


sum = count*(max*k+min) + plus*max
print(int(sum))

