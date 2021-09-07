import operator
import functools

def comparator(n1, n2): # [(재생횟수,고유번호), ...] 
    if n1[0] < n2[0]:  # 노래 재생 횟수
        return 1
    elif n1[0] == n2[0]:      
        return n1[1] - n2[1] # 노래 고유번호
    else:                  
        return -1
    
# comparator 의 return 값-> 양수(순서변경)
    
    
def solution(genres, plays):
    answer = []
    genre ={}
    
    for g in set(genres):
        genre[g]=[0]
    for i in range(len(plays)):
        genre[genres[i]][0]+=plays[i]
        genre[genres[i]].append((plays[i],i))
    # genre = {'classic': [1450, (500, 0), (150, 2), (800, 3)], 'pop': [3100, (600, 1), (2500, 4)]} 
    genre=sorted(genre.items(), key=operator.itemgetter(1),reverse=True)
    # genre = [('pop', [3100, (600, 1), (2500, 4)]), ('classic', [1450, (500, 0), (150, 2), (800, 3)])]

    for i in range(len(genre)):
        # genre[i] = ('pop', [3100, (600, 1), (2500, 4)])
        g=genre[i][1][1:]
        # g = [(600, 1), (2500, 4)]
        result = sorted(g, key=functools.cmp_to_key(comparator))
        # resut = [(2500, 4), (600, 1)]
        for i in result[:2]:
            answer.append(i[1])
    
    return answer