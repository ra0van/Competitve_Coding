#!/bin/python
#https://www.hackerrank.com/contests/w27/challenges/drawing-book
#Easy 10pts
import sys


n = int(raw_input().strip())
p = int(raw_input().strip())
# your code goes here

front = p/2
back = (n-p)/2

if front <back:
    print front
else:
    print back
