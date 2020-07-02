import sys
#sys.stdin = open("input.txt","rt")
N=int(input())
a=list(map(int, input().split()))
avg = round(sum(a)/N)
min=2100000000
for idx, x in enumerate(a):
    tmp = abs(x - avg) #abs():절댓값
    if tmp < min :
        min=tmp
        score=x
        i = idx + 1
    elif tmp == min :
        if x>score:
            score=x
            i=idx+1
print(avg,i)








