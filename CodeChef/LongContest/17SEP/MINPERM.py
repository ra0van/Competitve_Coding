t = input()
for _ in xrange(t):
    n = input()
    a = [i+1 for i in xrange(n)]
    i=0
    while i<n:
        if i+1<n:
            a[i],a[i+1] = a[i+1],a[i]
            # print a,'-',i,i+1
            i+=2
        else:
            break
    
    if n%2==1:
        a[n-2],a[n-1] = a[n-1],a[n-2]
    
    for i in a:
        print i,
    print "\n"
        