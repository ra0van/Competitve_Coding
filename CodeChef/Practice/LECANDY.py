# https://www.codechef.com/problems/LECANDY

t = int(raw_input())

while t:
	t-=1
	n,c = map(int,raw_input().split())
	a = map(int,raw_input().split())
	sum =0
	for i in range(n):
		sum += a[i]
	if sum<=c:
		print "Yes"
	else:
		print "No"
