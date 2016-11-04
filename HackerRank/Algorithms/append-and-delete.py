#!/bin/python

#https://www.hackerrank.com/contests/w25/challenges/append-and-delete
#11/12 passed 

import sys


def getCommonStart(a,b):
    if len(a) > len(b):
        a,b = b,a
    common = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            common += a[i]
        else:
            break
    
    return common


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())


if s==t:
    print "Yes"
elif k >= len(s) + len(t):
    print "Yes"
else:
    common = getCommonStart(s,t)
    if len(common)>0 and (len(s)+len(t) -  2*len(common) <= k):
        print "Yes"
    else:
        print "No"

