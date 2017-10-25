t = input()
for _ in xrange(t):
	n,p = map(int,raw_input().split())
	a = map(int,raw_input().split())
	e = int(p/2)
	h = int(p/10)
	cw,hp = 0,0
	for i in a:
		if i >= e:
			cw+=1
		if i <= h :
			hp +=1

	if cw==1 and hp==2:
		print 'yes'
	else: print  'no'
