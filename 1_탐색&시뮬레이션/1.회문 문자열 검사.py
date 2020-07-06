#팁:문자열을 모두 대문자로 바꾸면 비교하기가 쉽다
import sys
n=int(input())
for i in range(n):
  s=input()
  s=s.upper()
  size=len(s)
  for j in range(size//2):
    if s[j]!=s[-1-j]:
      print("#%d NO" %(i+1))
      break
  else:
    print("#%d YES" %(i+1))

#   s=s.upper()
#   if s==s[::-1]:   -> 문자열 reverse 시킨 것
#     print("#%d NO" %(i+1))
#   else:
#    print("#%d YES" %(i+1))
    
     



      
      
      
    
