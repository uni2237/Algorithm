import sys
sys.stdin=open("./input.txt")
input=sys.stdin.readline

n=int(input())
cards=sorted(list(map(int,input().split())))
m=int(input())
nums=list(map(int,input().split()))

# 
'''
from bisect import bisect_left, bisect_right

def count_num(num):
    start = bisect_left(cards , num)
    end = bisect_right(cards , num)
    return end-start


for i in nums:
    print(count_num(i),end=' ')
'''

# 리스트의 원소 갯수들을 count해서 dict로 변환해주는 Counter 함수 활용
from collections import Counter
c = Counter(cards)
# c = Counter({10: 3, -10: 2, 3: 2, 2: 1, 6: 1, 7: 1})
for n in nums:
    print(c[n] , end=' ')