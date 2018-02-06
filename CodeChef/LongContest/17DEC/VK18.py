def getD(n):
    odd = []
    even = []
    while n>0:
        r = n%10
        n = n/10
        if r%2==0:
            even.append(r)
        else:
            odd.append(r)
    return abs(sum(odd) - sum(even))

t = input()
ip = []
for _ in xrange(t):
    x = input()
    ip.append(x)
m = max(ip)

mRoom = m*2
d = []

for i in xrange(1,mRoom+1):
    d.append( getD(i))

# print d

for n in ip:
    start = 1
    end = start + n
    s = sum(d[start:end])
    prev = s  
    for i in xrange(1,n):
        # print start,end,
        prev -= d[start]
        prev += d[end]
        s += prev
        start += 1
        end += 1
        # print prev
    print s