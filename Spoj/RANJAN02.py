t = input()
a = [-1]*35
a[0]=2
for i in range(1,35):
	a[i] = a[i-1]*3
 
for i in range(t):
	n = input()
	print sum(a[0:n])
 
