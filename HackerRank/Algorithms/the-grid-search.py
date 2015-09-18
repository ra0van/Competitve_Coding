# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/the-grid-search
#partial 20/50
t = int(raw_input())
for i in range(t):
    r1,c1 = map(int,raw_input().split())
    g1 = ['']*r1
    for i in range(r1):
        g1[i] = g1[i]+raw_input()
    r2,c2 = map(int,raw_input().split())
    g2 = ['']*r2
    for i in range(r2):
        g2[i] = g2[i]+raw_input()
    
    found = False
    first = False
    posx = 0
    posy =0
    i = 0
    j = 0
    for i in range(r1-c2):
        if g2[0] in g1[i]:
            posx = i
            posy = g1[i].index(g2[0])
            first = True
            break;

    if first:
        i = 1
        j = 1
        found = True
        while i+posx<r1 and j<=r2-1:
            if g2[j] in g1[i+posx] :
                if posy != g1[i+posx].index(g2[j]):
                    #print i+posx,j
                    found = False
                    break
                j += 1
                i += 1
            else:
                #print i+posx,j
                found = False
                break

    if found:
        print "YES"
    else:
        print "NO"