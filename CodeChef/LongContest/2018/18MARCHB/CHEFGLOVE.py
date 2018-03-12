#https://www.codechef.com/MARCH18B/problems/CHEGLOVE
t = input()

while t>0:
    t-=1
    n = input()
    f = map(int,raw_input().split())
    g = map(int,raw_input().split())
    
    front,back = True,True
    
    for i in xrange(n):
        if f[i]>g[i]:
            front = False
            break
        
    for i in xrange(n):
        if f[n-i-1]>g[i]:
            back = False
            break
    
    if front and not back:
        print 'front'
    
    elif not front and back :
        print 'back'
    elif front and back :
        print 'both'
    else:
        print 'none'