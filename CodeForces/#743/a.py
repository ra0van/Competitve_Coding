'''
http://codeforces.com/contest/743/problem/A

Vladik and flights

'''

n,a,b = map(int,raw_input().split())
port = raw_input()

if a==b:
	print 0
else:
	if port[a-1] == port[b-1]:
		print 0
	else:
		print 1