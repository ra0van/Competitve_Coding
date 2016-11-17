# your code goes here
import math
t = input()

def SimpleSieve(size):
	a = [0]*(size+1)
	for i in range(2,size+1):
		if a[i] == 0 :
			j = 2
			while j*i<=size:
				a[j*i] = 1
				j+=1
	base = []
	for i in range(2,size+1):
		if a[i] == 0:
			base.append(i)
	return base

for i in range(t):
	x,y = map(int,raw_input().split())
	y=y
	limit = int(math.floor(math.sqrt(y))+1)
	base = SimpleSieve(limit)

	low = limit
	high = 2*limit
	for p in base:
		if p>= x:
			print p
	
	while low<y:
		# a = [0] *(high-low+1)
		mark = [True]*(limit+1)
		for p in base:
			lowLim = int(math.floor(low/p)*p)
			if lowLim<low:
				lowLim += p

			for j in range(lowLim,high,p):
				# print j,low,"in j low"
				mark[j-low] = False
		# print low,high
		for j in range(low,high):
			if mark[j-low]:
				if j>=x:
					print j
		low = low + limit
		high = high + limit
		if high >y:
			high = y

	print ""	
