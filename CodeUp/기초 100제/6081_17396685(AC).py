import sys
input= sys.stdin.readline

a=int(input(),16)
for i in range(1,16):
  print("%X"%a,"*%X"%i,"=%X"%(a*i),sep="")
#16진수 구구단
#int(input(),16) 으로 입력받은 문자를 16진수로 변환 
