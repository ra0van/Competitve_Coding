#IC
import math
def fib(n):
	diff = (phi**n) - (phi_1**n)
	val = int(diff / math.sqrt(5))
	return val
t = input()
phi_1 = (1.0 - math.sqrt(5))/2.0
phi = (1.0+math.sqrt(5))/2.0
m = [-1] * 
for i in range(t):
	m,n = map(int,raw_input().split())
	sum = 0
	for i in range(m,n+1):
		sum += fib(i)
	print sum%1000000007

