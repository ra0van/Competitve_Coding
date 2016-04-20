#https://www.hackerrank.com/contests/101hack36/challenges/super-functional-strings
#TLE 
def subs(str):
	l = len(str)
	return [str[i:j+1] for i in xrange(l) for j in xrange(i,l) ]


def Fun(s):
	d = len(set(s))
	l = len(s)
	return l**d % (1000000007)

t = input()
for tc in range(t):
    s = raw_input()
    # print subs(s)
    li = set(subs(s))
    subSum = 0
    for e in li:
    	subSum += Fun(e)
    print subSum

