import sys
input=sys.stdin.readline
a= int(input())

num = list(map(int, input().split()))
print(min(num)) # 제일 작은 값 출력
