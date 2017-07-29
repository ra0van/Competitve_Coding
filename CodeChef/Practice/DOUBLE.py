# https://www.codechef.com/problems/DOUBLE

t = int(raw_input())
while t:
	t -= 1
	n = int(raw_input())
	if n%2 == 0:
		print n
	else:
		print n-1