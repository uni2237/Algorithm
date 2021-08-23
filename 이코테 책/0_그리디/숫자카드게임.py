import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

n,m=map(int,input().split())

# 버전 1 : 각 행의 min값을 모두 저장해둔다음 한번에 max값 구하기
data=[]
for i in range(n):
    data.append(min(list(map(int,input().split()))))
print(max(data))


# 버전 2 : 매 행 마다 직전 행의 최솟값과 비교하기
result=0
for i in range(n):
    target=min(list(map(int,input().split())))
    result=max(target,result)
print(result)