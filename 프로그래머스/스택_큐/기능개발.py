from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progress=deque(progresses)
    speed=deque(speeds)
    
    while progress:
        count=0
        for i in range(len(progress)):
            progress[i]+=speed[i]
        while progress:
            if progress[0]>=100:
                count+=1
                progress.popleft()
                speed.popleft()
            else:
                break
        if count !=0:
            answer.append(count)
    
    return answer

print(solution([93, 30, 55]	,[1, 30, 5]))
