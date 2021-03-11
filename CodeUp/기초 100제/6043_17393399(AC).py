import sys
input= sys.stdin.readline
a,b= map(float,input().split())
c = float(a/b)
print('%.3f'% round(c,3))
# 소수점 아래 4번째에서 반올림 후 소수점 아래 3번째 까지 출력 
