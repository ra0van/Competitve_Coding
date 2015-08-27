# https://www.codechef.com/problems/CIELAB
a,b=map(int,raw_input().split())
c = a-b
last = c %10
if last <9 :
	c += 1
else:
	c -= 1
print c