#!/bin/python
#https://www.hackerrank.com/contests/may-world-codesprint/challenges/compare-the-triplets

import sys


a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

ap,bp = 0,0

for i in range(3):
    if a[i]>b[i]:
        ap+=1
    elif b[i]>a[i]:
        bp+=1

        
print ap,bp
 
