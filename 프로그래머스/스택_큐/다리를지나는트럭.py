from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=deque([0]*bridge_length)
    
    while True:
        if truck_weights:
            bridge.popleft()
            if truck_weights[0]+sum(bridge)>weight:
                bridge.append(0)
            else:
                bridge.append(truck_weights.pop(0))
            answer+=1  
        else:
            break
    
    for i in range(len(bridge)-1,-1,-1):
        if bridge[i]!=0:
            answer+=i+1
            break
        
    return answer