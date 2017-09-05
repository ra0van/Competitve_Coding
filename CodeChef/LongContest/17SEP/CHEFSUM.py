t = input()
for _ in xrange(t):
    n = input()
    a = map(int,raw_input().split())
    prefix = [a[0]]
    for i in xrange(1,n):
        prefix.append(prefix[i-1]+a[i])
    suffix = [sum(a)]
    
    for i in xrange(1,n):
        suffix.append(suffix[i-1]-a[i-1])
    
    mins = prefix[0] + suffix[0]
    minIndex = 0
    for i in xrange(1,n):
        s = prefix[i] + suffix[i]
        if s<mins :
            mins = s
            minIndex = i
        
    print minIndex+1
     