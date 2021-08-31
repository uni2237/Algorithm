def binary_search(start,end,n,times):
    result_mid=0
    while start<end:
        sum=0
        
        mid=(start+end)//2
        for t in times:
            sum+=mid//t
        print(start,end,sum,"명")

        if sum>=n:
            end=mid
        else:
            start=mid+1
    return start
    
def solution(n, times):
    answer = 0
    start=1
    end=n*max(times)
    
    answer=binary_search(start,end,n,times)

    return answer

print(solution(6, [7,10]))