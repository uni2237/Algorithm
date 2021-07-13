import sys
sys.stdin = open("Algorithm/input.txt","rt")
input = sys.stdin.readline

from collections import deque

t = int(input())

for _ in range(t):
    
    n , target= map(int,input().split())
    queue=deque(map(int,input().split()))
    sequence=deque([i for i in range(len(queue))])
    count=0
    if len(queue)==1:
        print(1)
        continue
    
    else: 
        while queue:
            m=max(queue)
            paper = queue.popleft()
            paper_i=sequence.popleft()


            if paper<m:
                queue.append(paper)
                sequence.append(paper_i)
            else:
                if paper_i==target:
                    count+=1
                    print(count)
                    break
                else:
                    count+=1
    
        
    
    