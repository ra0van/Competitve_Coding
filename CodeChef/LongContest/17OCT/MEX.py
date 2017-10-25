t= input()
for _ in xrange(t):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    m = max(a)
    a.sort()
    sa = set(a)
    sn = set([i for i in xrange(m+1)])
    sr = sn-sa
    if k==sr:
        print m+1
    elif k<len(sr):
        ar = list(sr)
        print ar[k]
    else:
        rem = k-len(sr)
        print m+rem+1
        
            