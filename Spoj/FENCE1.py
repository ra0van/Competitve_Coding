import math
while True:
	l = int(raw_input())
	if l==0:
		break;
	r = l/math.pi
	a = l**2/(2 * math.pi)
	print format(round(a,2),'.2f')
