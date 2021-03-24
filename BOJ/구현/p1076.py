#import sys
#input = sys.stdin.readline().rstrip

o = {'black': 0, 'brown':1 ,'red':2, 'orange':3, 'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
print((o[input()]*10 + o[input()])*(10**o[input()]))
