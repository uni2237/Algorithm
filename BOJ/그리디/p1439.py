import sys
sys.stdin = open("./input.txt")
input=sys.stdin.readline

s=input().rstrip()
# sys.stdin.readline은 끝에 개행('\n')이 들어감!
# rstrip으로 개행 없애주기

# 1,0 각각의 그룹 덩어리중 적은 덩어리 수가 정답
'''
a=s.split('0')
b=s.split('1')

a_len=len([n for n in a if n!=''])
b_len=len([n for n in b if n!=''])
print(min(a_len,b_len))
'''

# 0 또는 1로 변화하는 지점의 수 = count
# count에 1을 더해주고 총 2로 나눈 몫이 정답
count=0
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        count+=1
print((count+1)//2)
