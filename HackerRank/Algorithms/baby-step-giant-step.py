# https://www.hackerrank.com/contests/w25/challenges/baby-step-giant-step
#AC

t = input()
for i in range(t):
    a,b,d = map(int,raw_input().split())
    if d == 0:
        print 0
    elif d<a:
        print 2
    elif d==a:
        print 1
    elif d==b:
        print b
    elif d<b:
        print 2
    elif d>b:
        print d/b +1
        
        
