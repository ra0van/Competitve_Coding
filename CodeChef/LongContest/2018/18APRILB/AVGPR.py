t = input()
for _ in xrange(t):
    n = input()
    a = map(int,raw_input().split())
    odd = []
    even = []
    
    hash = {}
    
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
        hash[i] = 1
    
    pairs = 0
    
    for i in xrange(len(odd)):
        for j in xrange(i+1,len(odd)):
            x = (odd[i]+odd[j])/2
            if x in hash:
                pairs += 1
    
    # print len(even)
    for i in xrange(len(even)):
        for j in xrange(i+1,len(even)):
            # print i,j
            x = (even[i]+even[j])/2
            if x in hash:
                pairs += 1
                
    
    print pairs