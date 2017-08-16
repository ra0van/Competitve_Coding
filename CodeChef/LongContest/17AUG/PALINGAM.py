def solve(a,b):
    Na,Nb = [0]*26,[0]*26
    
    for i in a:
        Na[ord(i)-97] += 1
        
    for i in b:
        Nb[ord(i)-97] += 1
    
    #axa
    for i in xrange(26):
        if (2<= Na[i]) and (Nb[i] == 0):
            return True
    
    #aa
    result = False
    for i in xrange(26):
        if Na[i]!=0 and Nb[i]==0:
            result = True
            break
    if not result:
        return result
        
    result = False
    for i in xrange(26):
        if Na[i]==1 and Nb[i] == 0:
            result = True
            for j in xrange(26):
                if i!=j and Nb[j]==0 and Na[j] == 0:
                    result = False
                    break
            if result:
                return True
    
    return False
    
t = input()
for _ in xrange(t):
    a = raw_input()
    b = raw_input()
    if solve(a,b)==True:
        print 'A'
    else:
        print 'B'