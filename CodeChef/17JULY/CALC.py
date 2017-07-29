import math
t = input()
for _ in xrange(t):
  result = 0
  n,b = map(int,raw_input().split())
  mid = n/2
  midval = int(math.ceil(mid/float(b)))*b
  left = n - midval
  result = left * (midval/b)
  midval = int(math.floor(mid/float(b)))*b
  left = n - midval
  result = max(result,left * (midval/b))
    
  print result 
