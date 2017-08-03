#https://www.hackerearth.com/challenge/competitive/july-circuits-17/algorithm/fredo-and-sums-1-605205cd/

t = input()

for _ in xrange(t):
    n = input()
    a = map(int,raw_input().split())
    a.sort()
    
    smin = 0
    for i in xrange(0,n,2):
        if(i<n and i+1<n):
            smin += abs(a[i]-a[i+1])
    # print a 
    smax = 0
    for i in xrange(0,n/2):
        # print i,n-i,a[i],a[n-i-1]
        if(i<n and n-i-1<n) and i!=n-i-1:
            smax += abs(a[i]-a[n-i-1])
        
    
    print smin,smax
        
    