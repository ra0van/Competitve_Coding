t = input()
yes = 'YES'
no = 'NO'
for _ in xrange(t):
  s1,s2 = raw_input().split(" ")
  c1,c2 = set(s1),set(s2)
  flag = True
  if len(c1)>=len(c2):
    d1,d2 = '',''
    for i in xrange(len(s1)):
      if s1[i]!=s2[i]:
        d1 += s1[i]
        d2 += s2[i]
    
    f1= {}
    f2= {}
    for i in xrange(len(d1)):
      if d1[i] in f1:
        f1[d1[i]].append(i)
      else:
        f1[d1[i]] = [i]
        
      if d2[i] in f2:
        f2[d2[i]].append(i)
      else:
        f2[d2[i]] = [i]
      
    visited = [0]*len(d1)
    for i in xrange(len(d1)):
      if visited[i]==0:
        pos1 = f1[d1[i]]
        pos2 = f2[d2[i]]
        
        if pos1!=pos2:
          flag = False
          break
    
    if flag:
      print yes
    else:
      print no
  else:
    print no
