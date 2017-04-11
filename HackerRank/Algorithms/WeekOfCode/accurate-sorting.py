#!/bin/python

import sys


def isSortable(a):
    for i in range(0,len(a)-1):
        e = a[i]
        next_e = a[i+1]
        if e<next_e:
            continue
        elif e-next_e==1:
            a[i],a[i+1] = a[i+1],a[i]
        else:
            return 'No'
    return 'Yes'

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    # Write Your Code Here
    print isSortable(a)
        

