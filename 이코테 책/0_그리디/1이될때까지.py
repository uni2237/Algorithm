import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
n,k=map(int,input().split())

count=0

while True: # k로 최대한 많이 나눠야함!
    tmp=(n//k)*k 
    count+=n-tmp # k배수로 만들고 남은만큼 다 +1씩,
    n=tmp # n은 k배수로 갱신

    if n<k: # n이 k보다 작아져 더 나눌수 없음
        break
    
    n=n//k # k배수가 된 n을 k로 나눈 몫으로 갱신
    count+=1 # k로 나눠 줬으니까 +1 해줌

count+=n-1 # k로 못 나누고 남은 만큼 +1씩 해줌.
print(count)



