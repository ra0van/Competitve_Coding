t = input()
for _ in xrange(t):
  x,y = map(int,raw_input().split())
  v = x+y
  rank = v*(v+1)/2
  print rank + (v+1 - y)
  
  
