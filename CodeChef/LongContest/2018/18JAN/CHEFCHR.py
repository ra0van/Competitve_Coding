normal = 'normal'
lovely = 'lovely'
cases = input()
for _ in xrange(cases):
    s = raw_input()
    if len(s)<4:
        print normal
        continue
    prev = s[0:3]
    count = 0
    for i in xrange(3,len(s)):
        prev += s[i]
        if 'c' in prev and 'h' in prev and 'e' in prev and 'f' in prev:
            count += 1
        prev = prev[1:4]
    
    if count>0:
        print lovely,count
    else:
        print normal