a,b,c=map(int,input().split())
day=1
while day%a!=0 or day%b!=0 or day%c!=0:
  day+=1
print(day)

#a,b,c 최소공배수 쉽게 구하기
