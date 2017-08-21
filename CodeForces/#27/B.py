s = raw_input()
f = s[:3]
l = s[3:]
sf,sl = [],[]
for i in xrange(3):
    sf.append(int(s[i]))
    sl.append(int(s[3+i]))
repl = 0
while sum(sf)!=sum(sl):
    sf.sort()
    sl.sort()
    # print sf,sl
    diff = sum(sf)-sum(sl)
    if diff >0:
        sl,sf = sf,sl
    diff = abs(diff)
    maxd = 9-sf[0]
    if diff<=maxd:
        sf[0] += diff
    else:
        sf[0] += maxd
    
    repl += 1
# print sf,sl
print repl