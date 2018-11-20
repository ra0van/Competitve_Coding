t = input()
for _ in xrange(t):
    n = input()
    a = map(int,raw_input().split())
    value =0
    for i in xrange(n):
        for j in xrange(i+1,n):
            value = value ^ (a[i] + a[j]) ^ (a[i] + a[j])
        
        value = value ^ (a[i] + a[i])
    print value
        