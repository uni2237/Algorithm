import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

#좌-상하/우-상하/상-좌우/하-좌우
dx=[-1,+1,-1,+1,-2,+2,-2,+2]
dy=[-2,-2,+2,+2,-1,-1,+1,+1]

#ord() : 문자 -> 숫자
#chr(): 숫자 -> 문자

k= input()
row=int(k[1])
col=ord(k[0])-ord('a')+1
count=0

for i in range(8):
    nx=row+dx[i]
    ny=col+dy[i]
    if nx>0 and nx<9 and ny>0 and ny<9 :
        count+=1
print(count)


# dx,dy 말고 순서쌍 방법으로 하면?

steps=[(-2,-1),(-2,+1),(+2,-1),(+2,+1),(-1,-2),(-1,+2),(+1,-2),(+1,+2)]

for step in steps:
    nr=row+step[0]
    nc=col+step[1]
    if nr>0 and nr<9 and nc>0 and nc<9 :
        count+=1
print(count)