# version 1 - cmp_to_key 사용 / 두 수를 조합해서 큰 수가 나오는 순서대로 정렬
# a , b 일 때 문자열 조합 시  a+b > b+a 이면 a , b 순으로 정렬 
# ex) 9 , 90 -> a+b : 990 , b+a : 909 => 990이 909보다 큼(사전 순) -> 9가 우선순위
from functools import cmp_to_key
def comparator(a,b):
    ab,ba = a+b, b+a
    return int(ab) - int(ba)  # t1이 크다면 1, t2가 크다면 -1,  같으면 0

def solution(numbers):
    number = [str(n) for n in numbers]
    number = sorted(number, key=cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(number))) # ex) 0000 -> 0 으로 바꿔주기 위해 int로 바꿨다가 다시 문자열로 바꿔줌
    return answer

# version 2 - 숫자들을 문자열로 바꾼것을 *3해서 (1000이하니까) 비교 
#  ex) 9 , 90  -> 999, 909090 이므로 999가 더 큼(사전 순) -> 9가 우선순위
def solution(numbers): 
    numbers = list(map(str, numbers)) 
    numbers.sort(key=lambda x: x*3, reverse=True) 
    return str(int(''.join(numbers)))

# 내 풀이 - permutations 사용  / 다 시간초과.. ㅋ
import itertools
def solution(numbers): 
    numbers=list(map(str,numbers))
    a=list(map(''.join, itertools.permutations(numbers)))
    print(sorted(a)[-1])
solution([6,10,2])