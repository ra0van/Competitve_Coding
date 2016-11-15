#https://www.hackerrank.com/contests/ncr-codesprint/challenges/spiral-message
#AC
x,y = map(int,raw_input().split())

#Create immutable 2d array
a = [['']*y]*x
a = [t[:] for t in a]
for i in range(x):
    tmp = raw_input()
    a[i] = list(tmp)
    


d = 0

l = 0
r = y-1
t = 0
b = x-1
mesg = ''
while( l<=r and t<=b):
	if d == 0:
		for i in range(b,t-1,-1):
			mesg += a[i][l]
		l = l+1
		d=1
	elif d==1:
		for i in range(l,r+1):
			mesg += a[t][i]
		t = t+1
		d=2
	elif d==2:
		for i in range(t,b+1):
			mesg += a[i][r]
		r = r-1
		d = 3
	elif d==3:
		for i in range(r,l-1,-1):
			mesg += a[b][i]
		b=b-1
		d=0

	#print mesg
final = filter(None,mesg.split('#'))
print len(final)
