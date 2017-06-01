t = input()
for _ in xrange(t):
  s = list(raw_input().strip())
  l = len(s)
  eat = [0]*l
  
  scount = 0
  mcount = 0
  
  for i in xrange(l):
    if s[i] == 'm':
      if i-1>-1 and eat[i]==0:
        if s[i-1]=='s' and eat[i-1]==0 :
          s[i-1] = '*'
          eat[i] = 1
      if i+1<l and eat[i]==0:
        if s[i+1] == 's' and eat[i+1]==0:
          s[i+1] = '*'
          eat[i] = 1
      
  scount = s.count('s')
  mcount = s.count('m')
  #print scount,mcount,s,eat
  if scount == mcount:
    print 'tie'
  elif scount > mcount:
    print 'snakes'
  else:
    print 'mongooses'
      
