t = int(raw_input())

while t:
	t -= 1
	m = int(raw_input())
	n = int(raw_input())
	a = map(int,raw_input().split(' '))
	n1 = -1
	n2 = -1
	flag = False
	for i in range(n):
		val1 = a[i]
		if val1< m:
			for j in range(n):
				if m-val1 == a[j] and i!=j:
					n2 = j
					flag = True;
					break;

		if flag:
			n1 = i
			break;

	print n1+1,n2+1