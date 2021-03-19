import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	a,b = map(int,input().split())
	aa=a%10
	
	if aa == 0:
		print(10)
	elif aa in [1,5,6]:
		print(aa)
	elif aa in [4,9]:
		bb=b%2
		if bb == 0:
			print(aa*aa%10)
		else:
			print(aa)
	else:
		bb=b%4
		if bb ==0:
			print(aa**4%10)
		else:
			print(aa**bb%10)
      
      
# 처음 풀이 - 너무나도 당연한 시간 초과,,,
import sys 
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	a,b = map(int,input().split())
	c = str(a**b) 
	print(c[-1])
	
	
