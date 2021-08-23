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
    #result = (result > target) and result or target  와 같이 해도 됨.(삼항연산자 사용)

    # 파이썬 삼항연산자 -> ? 대신 and, : 대신 or 사용
    # 혹은 result = result if (result>target) else target
print(result)