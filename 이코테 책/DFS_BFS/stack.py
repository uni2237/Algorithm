stack=[] # 파이썬 기본 자료형인 list로 쉽게 stack 사용

# push가 append와 같음
stack.append(5)
stack.append(3)
stack.append(1)

# pop은 pop
stack.pop()

print(stack) #[5,3] 최하단부터 출력
print(stack[::-1]) #[3,5] 최상단부터 출력