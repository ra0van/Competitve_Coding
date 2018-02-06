#https://www.codechef.com/DEC17/problems/CPLAY

from sys import stdin
lines = stdin.readlines()
# lines = []
# for i in xrange(3):
#     lines.append(stdin.readline())

w1 = 'TEAM-A'
w2 = 'TEAM-B'
w = 'TIE'

for line in lines:
    #first round
    t1,t2 =0,0
    result = 0
    for i in xrange(0,10,2):
        if line[i] == '1':
            t1 += 1
        if abs(t2-t1)>=2 and i>5:
            result = i
            break
        if line[i+1] == '1':
            t2 += 1
        if abs(t2-t1)>=2 and i>5:
            result = i+1
            break
    if t1==t2:
        for i in xrange(10,20,2):
            if line[i] == '1':
                t1 += 1
            if line[i+1] == '1':
                t2 += 1
            if t1!=t2:
                break
        result= i+2
    
    if t1>t2:
        print w1,result
    elif t2>t1:
        print w2,result
    else:
        print w
        