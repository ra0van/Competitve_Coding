#TLE
import math
def SieveOfEratosthenes(upperBound,prev=0):
	# print "Se"
	li = []
	upperBoundSqrRoot = int(math.sqrt(upperBound))
	isComposite = [False]*(upperBound+1)

	for i in xrange(2,upperBoundSqrRoot+1):
		if not isComposite[i]:
			li.append(i)
			for k in xrange(i*i,upperBound+1,i):
				isComposite[k] = True

	for i in xrange(upperBoundSqrRoot,upperBound+1):
		if not isComposite[i]:
			if i not in li:
				li.append(i)
	return li

t = input()
prev = -1
li = []
for i in range(t):
	a,n = map(int,raw_input().split())
	if n>prev:
		del li[:]
		li = SieveOfEratosthenes(n)
		prev  = n
	for i in li:
		if i>=a and i<=n:
			print i

