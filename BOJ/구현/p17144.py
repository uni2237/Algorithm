import sys 
sys.stdin=open("Algorithm/input.txt","rt")
input = sys.stdin.readline

from copy import deepcopy 
 

def airclear(x, y, diff): #공기청정기 작동 
    for i in range(4): 
        while True: #공기청정기의 오른쪽 값부터 시작해서 공기청정기를 만나면 종료한다. 
            nowx, nowy = x+dx[diff[i]], y+dy[diff[i]] 
            if 0<=nowx<c and 0<=nowy<r and a[nowy][nowx] == -1: 
                return 
            if 0<=nowx<c and 0<=nowy<r: 
                a[nowy][nowx] = arr[y][x] 
            else: 
                break 
            x, y = nowx, nowy 
r, c, t = map(int, input().split()) 
a = [list(map(int, input().split())) for _ in range(r)] 
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 
air = [] #공기청정기의 좌표가 들어갈 큐 
for _ in range(t): 
    arr = [[0]*c for _ in range(r)] #동시에 확산이 이뤄지기때문에 확산을 시켜주는 동안 원래 미세먼지 값들이 변하면 안된다. 확산된 미세먼지 값들을 저장해줄 new 배열 
    for y in range(r): #확산 시작 
        for x in range(c): 
            if a[y][x] == 0: 
                continue 
            if a[y][x] == -1: #-1인 경우 공기청정기이므로, 좌표를 기록해준다. 
                arr[y][x] = -1 
                air.append([y,x]) 
                continue 
            flg = 0 
            for j in range(4):#if문을 통과했다면 미세먼지가 있는 곳이기 때문에 상하좌우로 미세먼지가 퍼지도록 해준다. 
                nowx, nowy = x+dx[j], y+dy[j] 
                if 0<=nowx<c and 0<=nowy<r and a[nowy][nowx]!=-1: 
                    arr[nowy][nowx] += a[y][x]//5 
                    flg += 1 
            arr[y][x] += a[y][x] - a[y][x]//5*flg 
    a = deepcopy(arr) #a=arr 을 하게되면 주소값이 저장돼서 deepcopy를 사용해준다. 
    y, x = air.pop() 
    airclear(x+1, y, [0, 2, 1, 3]) #공기청정기의 옆칸부터 공기청정을 시작한다. 
    #0,2,1,3은 x좌표증가->y좌표감소->x좌표감소->y좌표증가 를 하기 위한 리스트이다. 
    a[y][x+1] = 0 #공기청정기 옆칸은 0으로 바꿔준다. 
    y, x = air.pop() 
    airclear(x+1, y, [0, 3, 1, 2]) #0,3,1,2는 역시나 x좌표증가->y좌표증가->x좌표감소->y좌표감소 를 해주기 위한 리스트 
    a[y][x+1] = 0 
res = 0 
for i in range(r):
    res += sum(a[i]) 
print(res+2) #공기청정기의 값 두 개가 -1이므로 +2를 해준 값이 답이다.

