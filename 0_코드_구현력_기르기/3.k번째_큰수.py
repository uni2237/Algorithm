import sys
#sys.stdin = open("input.txt","rt")
N,K=map(int,input().split())
a=list(map(int,input().split()))
s=set() #list가 아닌 set을 쓰는 이유는 중복을 없애기 위함!
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s.add(a[i]+a[j]+a[k])
s=list(s)
s.sort(reverse=True)
print(s[K-1])

'''
set()
-add(): 집합에 요소 추가
-update():해당 집합에 다른 집합 추가 
-remove():집합에 해당 요소 제거
-clear():집합 내 모든 요소 제거
'''