#!/bin/python
#https://www.hackerrank.com/contests/101hack43/challenges/max-min-difference
#AC
import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

mina = [x for x in a]
maxa = [y for y in a]
mina.remove(min(a))
maxa.remove(max(a))

mind = max(mina)-min(mina)
maxd = max(maxa) - min(maxa)

if maxd<mind:
    print maxd
else:
    print mind
