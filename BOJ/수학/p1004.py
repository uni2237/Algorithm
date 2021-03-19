import sys 
input = sys.stdin.readline

def p1004(t):
	for _ in range(t):
		x1,y1,x2,y2 = map(int,input().split())
		n = int(input())
		count = 0
		for _ in range(n):
			cx,cy,r = map(int,input().split())
			if ( (cx-x1)**2 + (cy-y1)**2 )< r**2 and ( (cx-x2)**2 + (cy-y2)**2 ) <r**2:
				pass
			
			elif ( (cx-x1)**2 + (cy-y1)**2 )< r**2 :
				count +=1
			elif ( (cx-x2)**2 + (cy-y2)**2 ) <r**2 :
				count +=1
			
		print(count)
				
	
	
t = int(input())
p1004(t)

# 좌표가 원안에 있는 지 -> 원의 방정식으로 판별
# 원의 중심 : x,y , 임의의 점의 좌표: a,b , 원의 반지름 : r
# (x-a)^2 + (y-b)^2 < r^2 라면 점 (a,b)는 원안에 있음
