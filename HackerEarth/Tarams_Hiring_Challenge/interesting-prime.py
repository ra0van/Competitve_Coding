#https://www.hackerearth.com/tarams-python-developer-hiring-challenge/algorithm/interesting-prime/
#All TestCases Passed
# Time : 1.0062s

import math

combLi = []

def getComb(li,n,currLen,startLen,used):
    global combLi
    tmp = []
    for i in range(n):
        if used[i]:
            tmp.append(li[i])
    if tmp not in combLi:
        combLi.append(tmp)
    
    if currLen == n:
        return
    if startLen == n:
        return
    
    used[startLen]=True
    getComb(li,n,currLen+1,startLen+1,used)
    used[startLen]=False
    getComb(li,n,currLen,startLen+1,used)

def primeFactors(n):
    li = []
    while n%2==0:
        li.append(2)
        n = n/2
        # print n
    #print int(math.sqrt(n))+1
    for i in xrange(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            li.append(i)
            # print n,i
            n = n/i
    if n>2:
    	li.append(n)
    return li


t = int(raw_input())

for i in range(t):
    num = int(raw_input())
    li = primeFactors(num)
    if li==0:
        print 0
    else:
        li = sorted(li)
        # print li
#        used = [False] * len(li)
#        getComb(li,len(li),0,0,used)
        prev = None
        co = 1
        for item in li:
            if item!=prev:
                co *= li.count(item)+1
                prev = item
        print co-1