
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count=0
        p=prices[i]
        for j in range(i+1,len(prices)):
            count+=1
            if prices[j]<p:
                break
        answer.append(count)
    return answer
