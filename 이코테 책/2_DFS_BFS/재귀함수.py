def recurive(i):
    if i==10:
        return
    print(i,'번째 재귀함수에서 ',i+1,'번째 재귀함수 호출')
    recurive(i+1)
    print(i,'번째 재귀 함수 종료')
recurive(1)

''' 출력값
1 번째 재귀함수에서  2 번째 재귀함수 호출
2 번째 재귀함수에서  3 번째 재귀함수 호출
3 번째 재귀함수에서  4 번째 재귀함수 호출
4 번째 재귀함수에서  5 번째 재귀함수 호출
5 번째 재귀함수에서  6 번째 재귀함수 호출
6 번째 재귀함수에서  7 번째 재귀함수 호출
7 번째 재귀함수에서  8 번째 재귀함수 호출
8 번째 재귀함수에서  9 번째 재귀함수 호출
9 번째 재귀함수에서  10 번째 재귀함수 호출
9 번째 재귀 함수 종료
8 번째 재귀 함수 종료
7 번째 재귀 함수 종료
6 번째 재귀 함수 종료
5 번째 재귀 함수 종료
4 번째 재귀 함수 종료
3 번째 재귀 함수 종료
2 번째 재귀 함수 종료
1 번째 재귀 함수 종료

'''