n = input()
a = []
for i in xrange(n):
  p = input()
  a.append(p)

a.sort(reverse=True)

price = []
for i in xrange(n):
  price.append((i+1) * a[i])
  
print max(price)