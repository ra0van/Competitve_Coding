t = input()
for _ in xrange(t):
    s = raw_input()
    c = [0 for i in xrange(10)]
    
    for i in s:
        c[int(i)] += 1
    
    val = ''
    # print c
    for i in xrange(65,91):
        n1 = i%10
        n2 = i/10
        if n1==n2:
            if c[n1]>1:
                val += chr(i)
            continue
        if c[n1]>0 and c[n2]>0:
            # print i,c[n1],c[n2]
            val += chr(i)
    print val