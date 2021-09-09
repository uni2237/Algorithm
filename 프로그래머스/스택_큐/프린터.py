from collections import deque
def solution(priorities, location):
    answer = 0
    que=deque()
    for i,p in enumerate(priorities):
        que.append((p,i))
    
    while que:
        star=max(que)[0]
        top=que.popleft()
        
        if top[0]==star:
            answer+=1
            if top[1]==location:
                break
        else:
            que.append(top)
            
    return answer