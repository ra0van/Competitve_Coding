#partial TLE
n = input()
d = map(int,raw_input().split())

s = 0

for i in range(n-1):
	for j in range(i,n):
		if d[i]>d[j]:
			# print d[i],d[j]
			d[i],d[j] = d[j],d[i]
			s += (i-j)**2

# print d
print s