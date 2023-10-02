import sys
sys.stdin = open("./input.txt")
input=sys.stdin.readline

bar = list(input().rstrip())

stack = []
result=0

for i,b in enumerate(bar):
    if b == '(':
        stack.append(b)
    else: # ')' 일때
        if bar[i-1]=='(' :
            # 레이져인 경우 '()'
            stack.pop()
            result+=len(stack) # 막대기만큼 더해줌
        else:
            # 막대기 끝남 '))'
            stack.pop()
            result+=1
print(result)


