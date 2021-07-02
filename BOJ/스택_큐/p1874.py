import sys
sys.stdin = open("Algorithm\input.txt","rt")
input = sys.stdin.readline

array=[]
stack=[]
n=int(input())
for _ in range(n):
    stack.append(int(input()))
j=0
    


result=[]
for i in range(n):
    array.append(i+1)
    result.append('+')
    while len(array)!=0 and array[-1]==stack[j]:
        array.pop()
        j+=1
        result.append('-')
        

if (len(array)!=0):
    print('NO')
else:
    for x in result:
        print(x,end='\n')
