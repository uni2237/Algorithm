import sys
input = sys.stdin.readline

n = int(input())
d ={}

for _ in range(n):
	name = (input())[0]
	if name not in d:
		d[name] = 1
	else:
		d[name]+=1
a=[]
for i in d:
	if d[i]>=5:
		a.append(i)

if len(a)==0:
	print("PREDAJA")

else:
	a.sort()
	print("".join(a))
  
# 어떤 블로그에서 발견한 숏코딩
name = [raw_input()[0] for i in range(int(raw_input()))]
name = dict([[last,name.count(last)] for last in list(set(name)) if name.count(last)>=5])
print(''.join(sorted(name.keys())) if len(name)>=1 else 'PREDAJA')

#출처: https://qkqhxla1.tistory.com/601?category=685989 [archives]
