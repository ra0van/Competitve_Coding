#https://www.codechef.com/NOV16/problems/ALEXTASK

import sys

def gcd(a,b):
	if a==b:
		return a
	if a>b:
		return gcd(a-b,b)
	return gcd(a,b-a)
 
def lcm(a,b):
	return (a*b)/gcd(a,b)
		
 
t = input()
for k in range(t):
	n = input()
	a = map(int,raw_input().split())
	res = sys.maxint
	for i in range(n):
		for j in range(i+1,n):
			res = min(res,lcm(a[i],a[j]))
	
	print res
