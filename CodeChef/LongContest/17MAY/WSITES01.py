t = input()
 
n = []
flag = False
filters = []
 
def getString(s,p):
  pos = 1
  while '_'+s[0:pos] in p and pos < len(s):
    #print s,s[0:pos]
    pos +=1
  filters.append(s[0:pos])
 
p = '_'
for _ in range(t):
  si,st = raw_input().split()
  if si == '+':
    p += st
    p += '_'
  else:
    n.append(st)
 
for s in n:
  if '_'+s in p:
    print(-1)
    flag = True
    break
  else:
    getString(s,p)
 
if not flag:
  filters = sorted(set(filters))
  print len(filters)
  for x in filters:
    print x 
