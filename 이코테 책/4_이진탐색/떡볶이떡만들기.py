import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline

n,m=map(int,input().split())
array=list(map(int,input().split()))

def binary_search(n,m,array,start,end):
    result=0
    while start<=end:
        mid=(start+end)//2
        sum=0
        for i in array:
            if i>mid:
                sum+= i-mid
        if sum < m:
            end=mid-1
        else:
            result=mid
            start=mid+1

    return result

print(binary_search(n,m,array,0,max(array)))
