import sys
sys.stdin=open("Algorithm/input.txt","rt")
input=sys.stdin.readline

a,p=map(int,input().split())
d=[a]

while True:
    new_num=0
    for num in str(a):
        new_num+=int(num)**p
    
    if new_num in d:
        index=d.index(new_num)
        d=d[:index]
        print(len(d))
        break
    d.append(new_num)
    a=new_num
