while 1:
	n = int(raw_input())
	if n==-1:
		break;
	a = []
	sum=0
	for i in xrange(n):
		num = int(raw_input())
		a.append(num)
		sum += a[i]

	count=0;
	
	if sum%n==0:
		val = sum/n;
		for i in xrange(n):
			if a[i]<val:
				count += (val-a[i])

		print(count)

	else:
		print("-1")