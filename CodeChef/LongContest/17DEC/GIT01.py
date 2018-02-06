t = input()
for _ in xrange(t):
    x,y = map(int,raw_input().split())
    cake = []
    for i in xrange(x):
        line = raw_input()
        cake.append(line)
    # print cake
    
    p1,p2 = '',''
    for i in xrange(y):
        if(i%2==0):
            p1 += 'R'
            p2 += 'G'
        else:
            p1 += 'G'
            p2 += 'R'
    
    c1,c2 = [],[]
    for i in xrange(x):
        if(i%2==0):
            c1.append(p1)
            c2.append(p2)
        else:
            c1.append(p2)
            c2.append(p1)
    
    # print c1,c2
    
    #calculate cost to c1,c2
    
    cost1,cost2 = 0,0
    
    for i in xrange(x):
        for a,b in zip(cake[i],c1[i]):
            if a!=b:
                if a=='R':
                    cost1 += 5
                else:
                    cost1 += 3
                    
        for a,b in zip(cake[i],c2[i]):
            if a!=b:
                if a=='R':
                    cost2 += 5
                else:
                    cost2 += 3
    
    print min(cost1,cost2)