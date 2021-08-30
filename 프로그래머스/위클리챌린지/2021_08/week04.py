# 직업군 추천하기
import operator
def solution(table, languages, preference):
    answer = ''
    result={}
    for i in range(5):
        job_list=table[i].split(' ')
        job=job_list[0]
        scores=job_list[1:]
        sum=0
        for i,l in enumerate(languages):
            if l in scores:
                sum+=preference[i]*(5-scores.index(l))
        result[job]=-int(sum)
    
    new_result=sorted(result.items(), key=operator.itemgetter(1))
    

    if new_result[0][1]==new_result[1][1]:
        answer=min(new_result[0][0],new_result[1][0])
    else:
        answer=new_result[0][0]

    return answer

