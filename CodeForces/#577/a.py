#http://codeforces.com/contest/577/problem/A

n,x=map(int,raw_input().split())

arr = [[-1]*n]*n
count = 0
if x>n*n:
	print 0
else:
	for i in range(n):
		if x%(i+1)==0:
			if x/(i+1)<=n:
				count += 1
	print count

