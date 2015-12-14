t = input()
for i in range(t):

	val,n = map(int,raw_input().split())
	a = map(int,raw_input().split())
	a.sort(reverse=True)
	sum = 0
	count = 0
	print "Scenario #"+str(i+1)+":"
	if val ==0 :
		print 1
		continue
	for i in range(n):
		if sum>=val:
			break
		sum += a[i]
		count += 1
	if count>0 and sum>= val:
		print count
	else:
		print "impossible"
