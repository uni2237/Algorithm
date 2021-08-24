import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

dx=[-2,-2,2,2,-1,1,-1,1]
dy=[-1,1,-1,1,-2,-2,2,2]

#ord() : 문자 -> 숫자
#chr(): 숫자 -> 문자

where=input()
x=ord(where[0])-ord('a')
y=int(where[1])-1

count=0

for i in range(len(dx)):
    nx,ny=x+dx[i],y+dy[i]
    if 0<=nx<8 and 0<=ny<8:
        count+=1
print(count)



# dx,dy 말고 순서쌍 방법으로 하면?

steps=[(-2,-1),(-2,+1),(+2,-1),(+2,+1),(-1,-2),(-1,+2),(+1,-2),(+1,+2)]

for step in steps:
    nx=x+step[0]
    ny=y+step[1]
    if nx>0 and nx<8 and ny>0 and ny<8 :
        count+=1
print(count)
