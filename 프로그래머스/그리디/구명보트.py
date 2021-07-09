def solution(people, limit):
    
    answer = 1
    people.sort()

    i=0
    j=len(people)-1

    while i<j :

        if people[i]+people[j]<=limit:
            
            i+=1
            
        else:
            answer+=1
            
        j-=1
        
    return answer

print(solution([70, 50, 80, 50],100))

