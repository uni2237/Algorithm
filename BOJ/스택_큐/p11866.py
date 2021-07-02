import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

n,k=map(int,input().split())

from collections import deque
deque=deque()

for i in range(n):
    deque.append(i+1)

result=[]
while len(deque)>0:
    for _ in range(k-1):
        top=deque.popleft()
        deque.append(top)
    result.append(deque.popleft())
    

print("<", end='')
for i in result:
    if i == result[-1]:
        print(i, end = '>')
    else:
        print("%s, " %(i), end='')

    
    

''' 요세푸스
-> 1 2 3 4 5 6 7
-> 1 2   4 5 6 7
1 2 -> 4 5 6 7
1 2 -> 4 5   7
1 2 4 5 -> 7 (7,1,2 순으로 하면 2가 제거됨)
1   4 5 -> 7
1 -> 4 5 7
1 -> 4 5 
-> 1 4 5 
-> 1 4 
-> 1 4 
->   4 
다없어짐!
'''
