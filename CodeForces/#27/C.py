n = input()
a = []
for i in xrange(n):
    x  = map(int,raw_input().split())
    a.append(x)
a.sort()
px,py=0,0
flag =False
for [x,y] in a:
    if px==x:
        flag = True
        break
    if py>x :
        flag = True
        break
    px,py = x,y
if flag:
    print 'NO'
else:
    print 'YES'
    
    

