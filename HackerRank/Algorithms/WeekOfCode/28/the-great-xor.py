#https://www.hackerrank.com/contests/w28/challenges/the-great-xor
#!/bin/python

from sys import stdin,stdout


q = int(stdin.readline())
for a0 in xrange(q):
    x = long(stdin.readline().strip())
    # your code goes here
    count = 0
    for i in xrange(x):
        if i^x > x:
            count+=1
    print count
