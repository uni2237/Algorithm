import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline

n=int(input())
store=sorted(list(map(int,input().split())))
m=int(input())
want=sorted(list(map(int,input().split())))

# 이진 탐색 사용
def binary_search(store,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if store[mid]==target:
            return mid
        elif store[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

for i in want:
    result=binary_search(store,i,0,n-1)
    if result!=None:
        print('yes',end=' ')
    else:
        print('no',end=' ')


''' set 이용 -> 단순히 특정 데이터가 존재하는지 검사할때 매우 효과적!
n=int(input())
store=set(map(int,input().split()))

m=int(input())
li=list(map(int,input().split()))

for i in li:
    if i in store:
        print("yes",end=' ')
    else:
        print("no",end=' ')
'''


'''계수정렬 사용
n=int(input())
array=[0]*1000001

for i in input().split():
    array[int(i)]=1
m=int(input())
for i in list(map(int,input().split())):
    if array[i]==1:
        print('yes',end=' ')
    else:
        print('no',end=' ')
'''