# your code goes here
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
num=[]
s=1
for i in range(1,46):
	num.append([s,i])
	s+=i


sum=0
for i in range(a,b+1):
	for j in range(len(num)):
		if i>=num[j][0] and i < num[j+1][0]:
			sum+=num[j][1]
			break
print(sum)
