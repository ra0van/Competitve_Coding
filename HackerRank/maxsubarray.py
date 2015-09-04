# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/maxsubarray
def maxSubCont(a,n):
    max_upto_here = 0
    max_so_far = 0
    
    
    for i in xrange(n):
        max_upto_here += a[i]
        if max_upto_here<0:
            max_upto_here = 0
        if max_so_far<max_upto_here:
            max_so_far = max_upto_here
        
    return max_so_far

def maxSubNon(a,n):
    
    max_upto_here = 0
    max_so_far = 0
    
    for i in range(n):
        tmp =  max_upto_here + a[i]
        if max_upto_here < tmp:
            max_upto_here = tmp
    
    return max_upto_here
            
    
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    a = map(int,raw_input().split())
    isNeg = True
    mins = 0
    for i in range(n):
        if a[i]>=0:
            isNeg = False
            break
        if i==0:
            mins = a[i]
        elif a[i]>mins:
            mins = a[i]
    if isNeg:
        print mins,mins
    else:
        print maxSubCont(a,n), maxSubNon(a,n)