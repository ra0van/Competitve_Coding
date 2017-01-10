#!/bin/python
#https://www.hackerrank.com/contests/w28/challenges/boat-trip
import sys

no = "No"
yes = "Yes"

n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))
largest = max(p)
maxc = m*c
if maxc<largest:
    print no
else:
    print yes
