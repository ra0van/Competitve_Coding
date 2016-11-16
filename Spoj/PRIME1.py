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
	return baseO

for i in range(t):
	x,y = map(int,raw_input().split())

	limit = math.floor(math.sqrt(1000000000))
	base = SimpleSieve(limit)

	low = limit
	high = 2*limit

	prev = []
	while low<=y:
		a = [0] *(high-low+1)

		for p in base:




	
