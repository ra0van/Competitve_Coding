t = input()
for _ in range(t):
  n = input()
  a = map(int,raw_input().split())
  a.sort(reverse=True)
  b = a[:n]
  a = a[n:]
  print b[n/2]
  
  c = []
  for i in range(n):
    c.append(a[i])
    c.append(b[i])
  
  print ' '.join(map(str,c))  
