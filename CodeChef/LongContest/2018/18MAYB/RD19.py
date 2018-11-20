t = input()
for _ in xrange(t):
    n = input()
    a = map(int,raw_input().split())
    a.sort()
    if a[0]==1:
        print 0
    else:
        flag = False
        for i in xrange(1,n):
            if a[i]%a[0]!=0:
                flag = True
                break
        
        if flag:
            print 0
        else:
            print -1
