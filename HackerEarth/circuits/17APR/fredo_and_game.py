t = input()
for _ in range(t):
	a,n = map(int,raw_input().split())
	arr = map(int,raw_input().split())
	# gain = 3
	# loss = 1
	out = False
	for i in xrange(n):
		if a<1:
			# pint "breaking @ ",i,a
			out = True
			break;
		if arr[i]==1:
			a += 2
		else:
			a-=1
		# print a,
	# print i
	if out:
		print "No",i
	else:
		print "Yes",a