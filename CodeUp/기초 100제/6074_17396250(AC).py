import sys
input= sys.stdin.readline


a=int(ord(input().rstrip()))
start=ord('a')

while start<=a:
  print(chr(start),end=' ')
  start+=1

#a부터 입력받은 알파벳까지 출력
