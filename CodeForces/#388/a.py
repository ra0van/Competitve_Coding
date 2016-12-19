# http://codeforces.com/contest/749/problem/A

n = input()
if n%2==0:
	print n/2
	while n>0:
		print 2,
		n = n-2
else:
	print n/2+1
	print 3,
	n = n-3
	while n>0:
		print 2,
		n = n-2