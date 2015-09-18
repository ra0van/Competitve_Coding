#https://www.hackerrank.com/challenges/library-fine
# Enter your code here. Read input from STDIN. Print output to STDOUT
a1,b1,c1 = map(int,raw_input().split())
a2,b2,c2 = map(int,raw_input().split())
if c1>c2:
    print 10000
elif c1==c2:
    if b1>b2:
        print (b1-b2)*500
    elif b1==b2:
        if a1>a2:
            print (a1-a2)*15
        else:
            print 0
    else:
        print 0
else:
    print 0