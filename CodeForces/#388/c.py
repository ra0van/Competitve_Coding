#TLE

#http://codeforces.com/contest/749/problem/C

n = input()
vote = raw_input()

x = []
y = []

for i in range(n):
	if vote[i]=='D':
		x.append(i+1)
	else:
		y.append(i+1)

while len(x)>0 and len(y)>0:
	a = x[0]
	b = y[0]
	del x[0]
	del y[0]
	if a<b:
		x.append(a+n)
	else:
		y.append(b+n)

if len(x)>0:
	print 'D'
else:
	print 'R'
