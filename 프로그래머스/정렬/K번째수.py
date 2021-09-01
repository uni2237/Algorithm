def testcase(array,command):
    i,j,k=command
    return sorted(array[i-1:j])[k-1]
    
    

def solution(array, commands):
    answer = []
    
    for t in commands:
        answer.append(testcase(array,t))
    return answer