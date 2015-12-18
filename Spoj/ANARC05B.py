from sys import stdin,stdout
flag = False
while  flag != True:
	try:
		s = stdin.readline()
		if s=='0':
			flag = True
			continue
		a = map(int,s.split())
		l_a = a[0]
		a = a[1:]
		b = map(int,stdin.readline().rstrip("\n").split())
		l_b = b[0]
		b = b[1:]
		i=0
		j=0
		k=0
		c = list(set(a) & set(b))
		c = sorted(c, key = lambda k : a.index(k))
		# c = c[::-1]
		l_c = len(c)
		sum_a = 0
		sum_b = 0

		#print c
		l = []
		while i<l_a and j<l_b and k<l_c:
			if a[i]==b[j]==c[k]:
				# sum += max(sum_a,sum_b)
				l.append(max(sum_a,sum_b))
				l.append(a[i])
				i+=1
				j+=1
				k+=1
				# sum += a[i]
				# print sum
				sum_a = sum_b =0
				continue

			if a[i]!=c[k]:
				sum_a += a[i]
				i+=1
			if b[j]!=c[k]:
				sum_b += b[j]
				j+=1

		while i<l_a:
			sum_a += a[i]
			i+=1

		while j<l_b:
			sum_b += b[j]
			j+=1

		# sum += max(sum_a,sum_b)
		l.append(max(sum_a,sum_b))
		print sum(l)
	except :
		flag = True
		

