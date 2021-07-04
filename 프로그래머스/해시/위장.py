def solution(clothes):
    answer = 1
    dict={}
    for x in clothes:
        if x[1] not in dict:
            dict[x[1]]=1
        else:
            dict[x[1]]+=1
    
    for value in dict.values():
        
        answer*=(value+1) # 0까지 합함!!

    answer = answer -1 # 모두 0인경우 제외
    return answer