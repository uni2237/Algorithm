import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline

n,m=map(int,input().split())
money=[]
for _ in range(n):
    money.append(int(input()))

# 화폐 단위들이 큰단위가 작은 단위의 배수관계가 아니므로, 그리디처럼 큰 화폐단위부터 처리하는 방법 안 통함!!!!
d=[10001]*(m+1)
d[0]=0
for coin in money:
    for j in range(coin,m+1):
        d[j]=min(d[j],d[j - coin]+1)
if d[m]==10001:
    print(-1)
else:
    print(d[m])