import heapq

heap=[]
def solution(scoville, K):
    answer = 0
    for i in scoville:
        heapq.heappush(heap,i)
    
    while True:
        min1=heapq.heappop(heap)
        if min1 >=K:
            break
        if min1<K and len(heap)==0:
            answer=-1
            break
        min2=heapq.heappop(heap)
        new_min=min1+(min2*2)
        answer+=1
        heapq.heappush(heap,new_min)
    
    return answer