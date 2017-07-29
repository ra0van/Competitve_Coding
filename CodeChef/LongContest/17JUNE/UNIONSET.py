t = input()
for _ in xrange(t):
  n,k = map(int,raw_input().split())
  sets = []
  missing = []
  complete = [i for i in xrange(1,k+1)]
  for _i in xrange(n):
    tmp = map(int,raw_input().split())
    tmp = tmp[1:]
    sets.append(tmp)
    missList = list(set(complete) - set(tmp))
    missing.append(missList)
  
  #find sets which are already complete
  marked = [0]*n
  count = 0
  mcount = 0
  #print count,complete
  for _i in xrange(n):
    if len(missing[_i]) == 0 :
        count += (n-1-mcount)
        mcount += 1
        marked[_i] = 1
  for i in xrange(n-1):
    if marked[i] == 1:
      continue
    for j in xrange(i,n):
      if i==j:
        continue
      if marked[j] == 1:
        continue
      if set(sets[i]) | set(sets[j]) == set(complete) :
        #print set(sets[i]) | set(missing[i])
        count += 1
  
  print count
    
  
  
