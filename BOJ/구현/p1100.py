import sys
input = sys.stdin.readline

sum=0
c=[list(input()) for _ in range(8)]

for i in range(8):
	
	if i%2==0:
		for j in range(0,8,2):
			if c[i][j]=='F':
				sum+=1
	else:
		for j in range(1,8,2):
			if c[i][j]=='F':
				sum+=1
print(sum)
