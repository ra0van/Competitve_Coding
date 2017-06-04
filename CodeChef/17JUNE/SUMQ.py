t = input()
for _ in xrange(t):
  a,b,c = map(int,raw_input().split())
  x = map(int,raw_input().split())
  y = map(int,raw_input().split())
  z = map(int,raw_input().split())
  
  x = list(set(x))
  y = list(set(y))
  z = list(set(z))
  s = []
  for i in x:
    for j in y:
      for k in z:
        if i>j or j<k:
          continue
        s.append((i+j) * (j+k))
  #print s
  print(sum(s)%1000000007)
        
        
  
  
