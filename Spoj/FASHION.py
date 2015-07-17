t = int(raw_input())

while t:
	t-=1;
	n = int(raw_input())
	men = map(int,raw_input().split())
	women = map(int,raw_input().split())
	men.sort()
	women.sort()
	sum = 0
	for i in xrange(n):
		val =  (men[i]*women[i])
		sum += val
	print(sum)
