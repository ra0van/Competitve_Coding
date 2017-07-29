#partial TLE
t = input()
a =1
for _ in xrange(t):
  n,b = map(int,raw_input().split())
  maxb = n/b
  
  val = 0
  maxv = 0
  while maxb>0:
    bval = b*maxb
    aval = n-bval
    val = (aval*maxb)
    #print aval,bval,maxb
    if val>maxv:
      maxv = val
    maxb -= 1
  
  print maxv
  
