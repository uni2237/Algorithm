def solution(n, lost, reserve):
    answer = 0
    lost_=[]
    reserve_=[]
    for x in reserve:
        if x not in lost:
            reserve_.append(x)
            
    for x in lost:
        if x not in reserve:
            lost_.append(x)
            

    for x in reserve_:
        a=x-1
        b=x+1
        
        if a in lost_:
            lost_.remove(a)
        elif b in lost_:
            lost_.remove(b)

    return n-len(lost_)

