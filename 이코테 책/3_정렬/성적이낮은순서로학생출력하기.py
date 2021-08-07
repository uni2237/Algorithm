import sys
sys.stdin = open("Algorithm\input.txt","rt",encoding="UTF8")
input=sys.stdin.readline

n=int(input())

array=[]
for i in range(n):
    arr=input().split()
    array.append((arr[0],int(arr[1])))

def setting(data):
    return data[1]

array = sorted(array, key=setting)
'''
lambda 사용버전
array=sorted(array,key=lambda data:data[1])
'''
for a in array:
    print(a[0],end=" ")

# lambda 사용버전
array=sorted(array,key=lambda data:data[1])