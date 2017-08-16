t = input()
for _ in xrange(t):
    n,m = map(int,raw_input().split())
    minSalary = map(int,raw_input().split())
    offeredSalary,maxJobOffers,jobs = [],[],[]
    for i in xrange(m):
        a,b = map(int,raw_input().split())
        offeredSalary.append(a)
        maxJobOffers.append(b)
        jobs.append(b)
    
    #->m
    # |
    # n
    totalSalary = 0
    totalHired = 0
    qual = []
    for i in xrange(n):
        q = raw_input()
        qual.append(q)
        
        hasJob = False
        if '1' in q:
            hasJob = True
        if hasJob == False:
            continue
        maxSalary = 0
        maxSIndex = -1
        for j in xrange(m):
            if q[j]=='1' and offeredSalary[j]>=minSalary[i] and maxJobOffers[j]>0:
                if maxSalary<offeredSalary[j]:
                    maxSIndex = j
                    maxSalary = offeredSalary[j]
        if maxSIndex >=0:
            totalSalary += offeredSalary[maxSIndex]
            totalHired += 1
            maxJobOffers[maxSIndex] -= 1
            
    noHire = 0
    for j in xrange(m):
        if jobs[j] == maxJobOffers[j]:
            noHire += 1
            
    print totalHired,totalSalary,noHire