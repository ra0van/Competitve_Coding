# Partial
#https://www.hackerrank.com/contests/projecteuler/challenges/euler003
import math

def SieveOfEratosthenes(upperBound):
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


def primeFactors(num):
	pf = []
	while num%2==0:
		pf.append(2)
		num = num/2

	for i in xrange(3,int(math.sqrt(num))+1,2):
		while num%i==0:
			pf.append(i)
			num=num/i

	if num>2:
		pf.append(num)
	return pf

t = input()
prev = -1
for i in range(t):
	n = input()
	li = primeFactors(n)
	pn = max(li)
	if pn>prev:
		pn_li = SieveOfEratosthenes(pn)
		prev = pn

	li = sorted(li,reverse=True)
	for i in li:
		if i in pn_li:
			print i
			break

	# print li