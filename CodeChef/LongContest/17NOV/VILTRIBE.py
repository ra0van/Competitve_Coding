t = input()
for _ in xrange(t):
    s = raw_input()
    prev = ''
    aCount,bCount = 0,0
    skip = 0
    for i in s:
        if i == '.':
            skip +=1
        elif i == 'A':
            aCount+=1
            if prev==i:
                aCount += skip
            skip = 0
            prev = i
            # print aCount,bCount,skip
        elif i == 'B':
            bCount += 1
            if prev==i:
                bCount += skip
            skip = 0
            prev = i
            # print aCount,bCount,skip
    print aCount,bCount