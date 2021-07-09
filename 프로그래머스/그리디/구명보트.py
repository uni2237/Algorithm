def solution(people, limit):
    
<<<<<<< HEAD
    answer = 1
=======
    answer = len(people)
>>>>>>> 33610f7d6e0dbc1db70a19a86a6e95852ed71e3d
    people.sort()

    i=0
    j=len(people)-1

    while i<j :

        if people[i]+people[j]<=limit:
<<<<<<< HEAD
            
            i+=1
            
        else:
            answer+=1
            
=======
            answer-=1
            i+=1
            
>>>>>>> 33610f7d6e0dbc1db70a19a86a6e95852ed71e3d
        j-=1
        
    return answer

<<<<<<< HEAD
print(solution([70, 50, 80, 50],100))
=======

>>>>>>> 33610f7d6e0dbc1db70a19a86a6e95852ed71e3d

