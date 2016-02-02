#https://www.hackerrank.com/contests/hourrank-5/challenges/ann-jimmy

import sys
n = int(raw_input().strip())
# your code goes here
a = int(n/3)
n = n-a
b = int(n/2)
c = n-b
print a*b*c
