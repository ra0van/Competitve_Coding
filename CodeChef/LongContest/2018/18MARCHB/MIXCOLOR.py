t = input()
while t>0:
    t-=1
    n = input()
    a = map(int,raw_input().split())
    occ = {}
    for i in a:
        occ[i]=0
    
    for i in a:
        occ[i]+=1
    
    reps = 0
    for n,v in occ.items():
        reps += v-1
    
    print reps
    