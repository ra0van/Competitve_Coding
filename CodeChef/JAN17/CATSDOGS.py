#python2
#https://www.codechef.com/JAN17/problems/CATSDOGS
 
from sys import stdin,stdout
 
t = int(stdin.readline())
 
yes = 'yes\n'
no = 'no\n'
 
for i in range(t):
	c,d,l = stdin.readline().split()
	c = int(c)
	d = int(d)
	l = int(l)
	legs = 4
	maxc = d*2
	if maxc>c:
		maxc = c
	leftc = c-maxc
	min_legs = d*legs + leftc*legs
	max_legs = d*legs + c*legs
	
	if l%4!=0:
		stdout.write(no)
	else:
		if l < min_legs or l>max_legs:
			stdout.write(no)
			continue
		stdout.write(yes)
	
