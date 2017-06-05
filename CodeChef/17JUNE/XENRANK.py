t = input()
for _ in xrange(t):
  x,y = map(int,raw_input().split())
  v = x+y
  rank = v*(v+1)/2
  xi = 0
  yi = v
  ranks = []
  r = 1
  while xi <= v and yi >= 0 :
    if xi<=x and yi<=y:
      ranks.append(r)
    xi += 1 
    yi -= 1
    r += 1
  print rank + max(ranks)
  
  
  
