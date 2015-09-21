# https://www.hackerrank.com/contests/projecteuler/challenges/euler001
# failed for test case 5
def cal(n,val):
	sum = n*(n+1)/2
	sum *= val
	return sum

t = int(raw_input())

while t:
    t -= 1
    n = int(raw_input())
    sum = 0
    a = int((n-1)/3)
    b = int((n-1)/5)
    c = int((n-1)/15)
    if a>0:
    	sum+=cal(a,3)
	if b>0:
		sum += cal(b,5)
	if c>0:
		sum -= cal(c,15)

   	print sum