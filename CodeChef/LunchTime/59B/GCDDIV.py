def gcd( a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
t = input()
for _ in xrange(t):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    
    for j in xrange(n):
        for i in xrange(k,1,-1):
            if a[j]%i==0:
                a[j]=a[j]/i
                break
    
    # print a

    g = a[0]
    for i in xrange(n-1):
        g = gcd(a[i],g)
    
    if g==1:
        print 'YES'
    else:
        print 'NO'
    

    
    