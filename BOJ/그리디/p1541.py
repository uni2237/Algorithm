import sys
sys.stdin = open("Algorithm/input.txt","rt")
input = sys.stdin.readline
string = input().split('-') 
print(string)
sum = 0 
for n in string[0].split('+'): 
    sum += int(n) 

for st in string[1:]: 
    for n in st.split('+'): 
        sum -= int(n) 
print(sum)

