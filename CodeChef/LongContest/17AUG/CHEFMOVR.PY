t = input()
for _ in xrange(t):
	n,d = map(int,raw_input().split())
	a = map(int,raw_input().split())
	avg = sum(a)/n
	res = 0
	
	for i in xrange(n-d):
		if a[i]<avg:
			diff = avg-a[i]
			a[i] += diff
			a[i+d] -= diff
			res += diff
		elif a[i]>avg:
			diff = a[i]-avg
			a[i] -= diff
			a[i+d] += diff
			res += diff
	flag = True
	for i in xrange(n):
		if a[i] != avg:
			flag = False
			break
	
	#print a
	if flag:
		print res
	else:
		print -1