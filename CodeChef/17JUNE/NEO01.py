t = input()
for _ in xrange(t):
  n  = input()
  a = map(int,raw_input().split())
  s = []
  t = []
  for i in a:
    if i<0:
      s.append(len(t) * sum(t))
      s.append(i)
      t = []
    else:
      t.append(i)
  
  if len(t)>0:
    s.append(len(t) * sum(t))

  print sum(s)
  
  
  
