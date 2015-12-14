import math

def check(val):
	if val in a:
		return a[val]
	else:
		a[val] = math.factorial(val)
		return a[val]

t= input()
a = {}
for i in range(t):
	n,k=map(int,raw_input().split())
	div = 1
	f = max(k-1,n-k)
	for i in range(f+1,n):
		# print i
		div *= i
	# print div,f_k
	f_k = check(min(k-1,n-k))
	print div/f_k


