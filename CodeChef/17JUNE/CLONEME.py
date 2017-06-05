t = input()
for _ in xrange(t):
  n,q = map(int,raw_input().split())
  arr = map(int,raw_input().split())
  
  for q1 in xrange(q):
    a,b,c,d = map(int,raw_input().split())
    a1 = arr[a-1:b]
    a2 = arr[c-1:d]
    a1.sort()
    a2.sort()
    dis = 0
    for i in xrange(len(a1)):
      if a1[i]!=a2[i]:
        dis += 1
    if dis > 1:
      print 'NO'
    else:
      print 'YES'
  
