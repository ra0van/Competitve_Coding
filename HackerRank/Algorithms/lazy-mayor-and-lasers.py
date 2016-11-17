#https://www.hackerrank.com/contests/101hack40/challenges/lazy-mayor-and-lasers
#TLE
n = input()
a = map(int,raw_input().split())
l = input()
b = map(int,raw_input().split())

for j in range(l):
	laser = b[j]-1
	for i in range(b[j]-1):
		if a[i] > laser:
			a[i] = laser
		laser -= 1
        #print a
print sum(a)