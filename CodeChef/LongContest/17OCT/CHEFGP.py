def fill(a,b,x,y,p,q):
	ma = a/x
	mb = b/y
	ra = a%x
	rb = b%y
	ca,cb = ma,mb
	if ra>0:
		ca = ma+1
	if rb>0:
		cb = mb+1
		
	pb = b/(ca-1)
	
	setb = min(y,pb)
	
	
	
t = input()
for _ in xrange(t):
	s = raw_input()
	x,y = map(int,raw_input().split())
	a,b = 0,0
	l = 0
	for i in s:
		if i=='a':
			a += 1
		else:
			b += 1
		l+=1	
	ma = a/x
	mb = b/y
	if ma>mb:
		fill(a,b,x,y,'a','b')
	else:
		fill(b,a,y,x,'b','a')