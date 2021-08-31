def binary_search(start,end,n,times):
    
    while start<end:
        sum=0
        
        mid=(start+end)//2
        for t in times:
            sum+=mid//t
        
        if sum>=n:
            end=mid
        else:
            start=mid+1
    return start # start를 반환함으로 최소시간을 구함!!
    
def solution(n, times):
    answer = 0
    start=1
    end=n*max(times)
    
    answer=binary_search(start,end,n,times)

    return answer

