t = input()
for _ in xrange(t):
  n  = input()
  a = map(int,raw_input().split())
  neg = []
  psum = 0
  pcount = 0
  for i in a:
    if i < 0:
      neg.append(i)
    else:
      psum += i
      pcount += 1
  
  neg.sort(reverse=True)
  total = 0
  pval = psum * pcount
  for negative in neg:
    neg_sum = (psum+negative)*(pcount+1)
    if neg_sum > pval:
      pval = neg_sum
      psum += negative
      pcount += 1
    else:
      total += negative

  print total + (pval)
  
  
  
