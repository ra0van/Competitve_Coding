#!/bin/python

#https://www.hackerrank.com/contests/w25/challenges/between-two-sets
#AC

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

start = max(a)
end = min(b)

if(start>end):
    print 0
elif start == end:
    print 1
else:
    count = 0
    for i in range(start,end+1):
        isHCF = True
        isLCM = True
        for e in a:
            if i%e!=0:
                isHCF = False
                break;
        for e in b:
            if e%i!=0:
                isLCM = False
                break
        
        if isLCM and isHCF:
            #print i
            count += 1
    
    print count
