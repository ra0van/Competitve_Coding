# your code goes here
t = input()
for i in range(t):
	a,b = map(int,raw_input().split())
	c = b%4
	if b!=0 and c==0:
		c=4
	a = a**c
	print str(a)[-1:]
