def solution(answers):
    answer = []
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    sum_a=0
    sum_b=0
    sum_c=0
    for i,j in enumerate(answers):
        if a[i%5]==j:
            sum_a+=1
        if b[i%8]==j:
            sum_b+=1
        if c[i%10]==j:
            sum_c+=1
    array=[sum_a,sum_b,sum_c]
    m=max(array)
    if sum_a==m:
        answer.append(1)
    if sum_b==m:
        answer.append(2)
    if sum_c==m:
        answer.append(3)
    
    return answer
print(solution([1,2,3,4,5]))