from collections import deque
import copy
def solution(numbers, target):
    answer = 0
    queue=deque()
    queue.append(numbers[0])
    queue.append(-numbers[0])
    for i in range(1,len(numbers)):
    	
    	for _ in range(len(queue)):
            q=queue.popleft()
            queue.append(q+numbers[i])
            queue.append(q-numbers[i])
	
    for q in queue:
        if q==target:
            answer+=1
    return answer
