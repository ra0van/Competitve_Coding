#!/bin/python
#https://www.hackerrank.com/challenges/saveprincess
def displayPathtoPrincess(n,grid):
    mPos = []
    pPos = []
    mFound = False
    pFound = False
    i = 0
    # print grid
    while (mFound!=True or pFound!=True )and i<n:
        if 'm' in grid[i]:
            mPos.append(i)
            mPos.append(grid[i].index('m'))
            mFound == True
        if 'p' in grid[i]:
            pPos.append(i)
            pPos.append(grid[i].index('p'))
            pFound = True
        i += 1
    
    x1 = mPos[0]
    y1 = mPos[1]

    x2 = pPos[0]
    y2 = pPos[1]

    if y1<y2:
    	print "RIGHT\n"*(y2-y1),
    if y1>y2:
    	print "LEFT\n"*(y1-y2),
    if x1>x2:
    	print "UP\n"*(x1-x2),
    if x1<x2:
    	print "DOWN\n"*(x2-x1),

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
