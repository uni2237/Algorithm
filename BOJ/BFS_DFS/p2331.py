def next(A,P):
    a=str(A)
    answer=0
    for i in a:
        answer+=pow(int(i),P)
    return answer
 
def dfs(A,P,count,check):
    if check[A]!=0:
        return check[A]-1
    check[A]=count
    b= next(A,P)
    count+=1
    return dfs(b,P,count,check)
 
 
check=[0]*250000
A, P =map(int,input().split())
count=1
print(dfs(A,P,count,check))
