#!/bin/python
#https://www.hackerrank.com/challenges/saveprincess2
def nextMove(n,r,c,grid):
    pPos = []
    pFound = False
    i = 0
    while  pFound!=True and i<n:
        if 'p' in grid[i]:
            pPos.append(i)
            pPos.append(grid[i].index('p'))
            pFound = True
        i += 1
    mPos = [r,c]
    pri = False
    x1 = mPos[0]
    y1 = mPos[1]

    x2 = pPos[0]
    y2 = pPos[1]

    if y1<y2 and pri!=True:
        return "RIGHT"
    if y1>y2 and pri!=True:
        return "LEFT"
    if x1>x2 and pri!=True:
        return "UP"
    if x1<x2 and pri!=True:
        return "DOWN"
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
