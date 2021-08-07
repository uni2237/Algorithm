import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline


#북동남서
dx=[-1,0,+1,0]
dy=[0,+1,0,-1]

n,m=map(int,input().split())
d=[[0]*m for _ in range(n)]


x,y,direction=map(int,input().split())
d[x][y]=1

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

def turn_left():
    # 북(0)->서(3)
    # 동(1)->북(0)
    # 남(2)->동(1)
    # 서(3)->남(2)  
    global direction  # 함수 밖에서 global로 전역변수 선언해도, 함수 안에서 global 명시 안하면 지역변수로 처리됨 !!!!!!  함수안에서 global 명시 해주자!
    direction= (direction+3)%4
    

count=1
no_turn=0

while True:
    turn_left() #왼쪽 회전
    nx=x+dx[direction]
    ny=y+dy[direction]

    # 아직 방문 x 
    if d[nx][ny]==0 and arr[nx][ny]==0:
        d[nx][ny]=1
        count+=1
        x=nx
        y=ny
        no_turn=0
        continue

    # 방문했거나 바다
    else:
        no_turn+=1
    
    # 4번 다 갈곳 x
    if no_turn==4:
        nx=x-dx[direction]
        ny=y-dy[direction]

        # 뒤가 육지, 갈수있음
        if arr[nx][ny]==0:
            x=nx
            y=ny
        # 뒤가 바다라 못감
        else:
            break
        
        no_turn = 0 # 다시 0으로 초기화

print(count)

#입력
#4 4 
#1 1 0 
#1 1 1 1 
#1 0 0 1 
#1 1 0 1 
#1 1 1 1