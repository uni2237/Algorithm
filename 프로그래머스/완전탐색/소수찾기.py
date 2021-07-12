from itertools import permutations
import math


def solution(numbers):
    answer = 0
    array=[]
    for i in range(1,len(numbers)+1):
    	array.append(list(map(''.join, permutations(numbers,i))))
    arr=set(list(map(int,sum(array,[]))))

    for n in arr:
        if n<2 :
            continue
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            answer+=1
            
    return answer
    