import math
def SieveOfEratosthenes(upperBound):
	li = []
	upperBoundSqrRoot = int(math.sqrt(upperBound))
	isComposite = [False]*(upperBound+1)

	for i in xrange(2,upperBoundSqrRoot):
		if not isComposite[i]:
			li.append(i)
			for k in xrange(i*i,upperBound,i):
				isComposite[k] = True

	for i in xrange(upperBoundSqrRoot,upperBound):
		if not isComposite[i]:
			li.append(i)

	return li

n = input("enter number")

li = SieveOfEratosthenes(n)
print li
