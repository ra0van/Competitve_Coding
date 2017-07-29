#https://www.codechef.com/ISCC2017/problems/PATROL
t = input()
for _ in xrange(t):
  u,v,x = map(int,raw_input().split())
  y = str(u+v) + '.0'
  x = x/float(y)
  print '{0:.10f}'.format(x)
