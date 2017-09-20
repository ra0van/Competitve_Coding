def executeCommand(q,i,ip,qcount):
    if q[i][0] == 1:
        # updateTree(ip,q[i][1]-1,q[i][2]-1)
        qcount[i]+=1
    else:
        for j in xrange(q[i][1],q[i][2]+1):
            executeCommand(q,j-1,ip,qcount)
 
def updateTree(ip,x,y,val):
    ip[x] += val
    ip[y+1] -= val
 
t = input()
for _ in xrange(t):
    n,m = map(int,raw_input().split())
    q = []
    qcount = [0]*m
    ip = [0]*(n+1)
    for i in xrange(m):
        tq = map(int,raw_input().split())
        q.append(tq)
        executeCommand(q,i,ip,qcount)
    print qcount
    for i in xrange(m):
        if qcount[i]>0:
            updateTree(ip,q[i][1]-1,q[i][2]-1,qcount[i])
    
    s = 0
    for i in xrange(n):
        s += ip[i]
        print s,
    print "\n"