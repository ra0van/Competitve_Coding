t = input()
for _ in xrange(t):
    p1,p2,k = map(int,raw_input().split())
    total = p1+p2
    rounds = total/k
    if rounds%2 ==0 :
        print "CHEF"
    else:
        print "COOK"