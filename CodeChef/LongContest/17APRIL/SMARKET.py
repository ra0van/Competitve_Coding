t = int(input())
for idx in range(t):
  n,q = map(int,raw_input().split())
  stock = map(int,raw_input().split())
  prev = -1
  dp = [0]
  for i in xrange(n):
    if stock[i]==prev:
      dp.append(dp[i]+1)
    else:
      dp.append(1)
      prev = stock[i]
  # print dp
  for i in xrange(q):
    l,r,k = map(int,raw_input().split())
    newDp = dp[l:r + 1]
    # print newDp;
    dip = False
    j = 0
    prev = dp[l-1]
    if l!=1:
      while not dip and j<len(newDp):
        if newDp[j] <= prev:
          dip = True
        else:
          prev = newDp[j]
          newDp[j] -= dp[l-1]
        j+=1
    newDp.insert(0,0)
    
    count = 0
    end = len(newDp)-1
    dip = False
    #print newDp
    for j in range(end):
      if newDp[j+1]<=newDp[j]:
        if newDp[j]>=k:
          #print 'dip',newDp[j+1],newDp[j]
          count += 1
    if  newDp[j+1]>=k:
        #print 'dip',newDp[j+1],newDp[j]
        count +=1 
    print count
