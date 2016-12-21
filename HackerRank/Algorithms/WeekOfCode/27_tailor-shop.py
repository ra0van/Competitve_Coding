#!/bin/python
#https://www.hackerrank.com/contests/w27/challenges/tailor-shop
#AC
'''
  Initially TLE when max(values) was used.
  Don't use max([]) or min([])
'''
import sys

n,p = raw_input().strip().split(' ')
n,p = [int(n),int(p)]
a = map(int,raw_input().strip().split(' '))
# your code goes here
values = []
maxv = 0
for i in range(n):
    minp = 0
    min = a[i]/p
    if a[i]%p!=0:
        min +=1
    if min not in values:
        minp = min*p
        values.append(min)
    else:
        min = maxv+1
        minp = min*p
        values.append(min)
    if maxv<min:
        maxv=min
print sum(values)
        


