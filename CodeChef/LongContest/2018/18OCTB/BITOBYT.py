tc = input()
for _ in xrange(tc):
    n = input()-1
    population = int(2.0 ** (n/26))
    remaining = n%26
    
    if (remaining >= 0 and remaining < 2) :
	    print population ,0,0
    elif (remaining >= 2 and remaining < 10) :
        print 0, population , 0
    elif (remaining >= 10 and remaining < 26) :
        print 0,0, population
