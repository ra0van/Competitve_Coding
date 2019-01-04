n = input()
s = raw_input()
ind = 1
i = 0
res = ''
while i<n:
    res += s[i]
    for j in xrange(ind):
        i += 1
    ind += 1
print res
