#https://www.codechef.com/FEB16/problems/STROPR
#TLE for few test cases
t = input()
for i in range(t):
	n,x,m = map(int,raw_input().split())
	a = map(int,raw_input().split())
	for j in range(m):
		for k in range(1,x):
			a[k] = a[k] + a[k-1]
			print a
	print a[x-1]%(1000000007)
