# 이진탐색 기본 코드

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))


# 1. 재귀 사용
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        binary_search(array,target,start,mid-1)
    else:
        binary_search(array,target,mid+1,end)


# 2. 반복문 사용
def binary_search(array,target,start,end):
    while start<=end:
        
        mid=(start+end)//2
    
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None


# 결과

result = binary_search(array, target, 0, n - 1) 

if result == None:
    print("원소가 존재하지 않습니다.") 
else:
    print(result + 1)