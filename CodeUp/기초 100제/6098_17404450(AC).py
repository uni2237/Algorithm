import sys
input=sys.stdin.readline

maze = [list(map(int,input().split())) for _ in range(10)]


x=1
y=1

while True:
  
  if maze[x][y] == 2:
    maze[x][y]=9
    break
    
  elif maze[x][y+1]== 1: # 우측 1, 아래로 가야함
    if maze[x+1][y] == 1: #아래도 1이라 막혀있다면
      maze[x][y]=9
      break # 더이상 못가고 멈춤
    else:
      maze[x][y]=9
      x+=1
  else : #우측 0
    maze[x][y]=9
    y+=1 


for i in range(len(maze)):
  print(*maze[i])
