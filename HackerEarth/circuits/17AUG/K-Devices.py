import math
n,k = map(int,raw_input().split())
x = map(int,raw_input().split())
y = map(int,raw_input().split())
distance = []
sq = []
for i in xrange(n):
    z = (x[i]**2) + (y[i]**2)
    distance.append(math.sqrt(z))

distance.sort()

r = distance[k-1]
# print r,round(r)
if round(r)<r:
    print int(r)+1
else:
    print int(r)
