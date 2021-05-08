from collections import deque

# 파이썬에선 deque를 큐로 씀! 그냥 큐보다 빠름
queue =deque()

# enqueue는 append
queue.append(5)
queue.append(3)
queue.append(1)

# dequeue는 popleft()
queue.popleft() 

print(queue) # deque([3,1]) => 먼저 들어온 것부터 출력
queue.reverse() 
print(queue) # deque([1,3]) -> 나중에 들어온 것부터 출력


######## deque 설명 ########
# 스택과 큐의 장점 모두 채택 -> 삽입,삭제 속도 빠름
# list(queue) 하면 리스트로 반환가능
