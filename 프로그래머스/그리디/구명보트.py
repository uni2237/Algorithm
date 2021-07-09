def solution(people, limit):
    
    answer = len(people)
    people.sort()

    i=0
    j=len(people)-1

    while i<j :

        if people[i]+people[j]<=limit:
            answer-=1
            i+=1
            
        j-=1
        
    return answer



