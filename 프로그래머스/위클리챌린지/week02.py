def solution(scores):
    answer = ''
    index=0
    n=len(scores)
    for _ in range(n):
        score=[]
        average=0
        self_score=scores[index][index]
        for j in range(n):
            if j!=index:
                score.append(scores[j][index])
        if self_score>max(score) or self_score<min(score):
            average=sum(score)/(n-1)
        else:
            average=(sum(score)+self_score)/n

        if average>=90:
            answer+='A'
        elif average>=80:
            answer+='B'
        elif average>=70:
            answer+='C'
        elif average>=50:
            answer+='D'
        else:
            answer+='F'


        index+=1


    return answer