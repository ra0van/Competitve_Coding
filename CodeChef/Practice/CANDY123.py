t = input()

for _ in xrange(t):
    l,b = map(int,raw_input().split())
    count =0
    l_c,b_c = 0,0
    limak,bob= False,False
    i = 0
    
    while True:
        count +=1 
        if i%2==0:
            l_c += count
            if l_c >l:
                limak = True
                break
        
        else:
            b_c += count
            if b_c>b:
                bob = True
                break
        
        i+=1
    
    if bob:
        print 'Limak'
    else:
        print 'Bob'