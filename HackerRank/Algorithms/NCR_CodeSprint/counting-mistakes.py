#!/bin/python
#https://www.hackerrank.com/contests/ncr-codesprint/challenges/counting-mistakes
import sys


n = input()
a = map(int,raw_input().strip().split())

m = 0
for i in range(n):
    if i==0:
        if a[i]!=1:
            m+=1
    elif a[i]-a[i-1]!=1:
        m+=1
        
print m

