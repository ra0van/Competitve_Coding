# your code goes here
def mod(num):
	if num<0:
		return num*(-1)
	return num

def checkIfFunny(s):
	rev = s[::-1]
	l = len(s)
	
	for i in xrange(1,l,1):
		a = mod(ord(s[i])-ord(s[i-1]))
		b = mod(ord(rev[i]) - ord(rev[i-1]))
	#	print(ord(s[i])-ord(s[i-1]))
	#	print(ord(rev[i]),ord(rev[i-1]))
		if(a!=b):
		#	print(a)
		#	print(b)
			return "Not Funny"

	return "Funny"

t = int(raw_input())

while t:
	t -=1
	s = raw_input()
	print(checkIfFunny(s))