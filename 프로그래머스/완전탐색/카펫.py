import math
def solution(brown, yellow):
    array = []
    answer=[]
    for x in range(1, int(math.sqrt(yellow))+1):
        if yellow%x==0:
            array.append([x+2,yellow//x+2])  


    for i in array:
        
        if (i[0])*(i[1])==(brown+yellow):
            i.sort(reverse=True)
            answer=i
            break
    return answer


