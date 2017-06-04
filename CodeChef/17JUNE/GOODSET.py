t1 = input()
ip = []
op = []
 
t = 1
for i in xrange(500):
  op.append(t)
  t += 2
 
for i in xrange(t1):
  ip = input()
  for j in xrange(ip):
    print op[j],
