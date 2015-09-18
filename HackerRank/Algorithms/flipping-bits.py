import string

def flipBits(s):
	a = string.replace(s,'0','2')
	a = string.replace(a,'1','0')
	a = string.replace(a,'2','1')
	#print(a)
	return a

t = int(raw_input())

while t:
	t -= 1
	num = int(raw_input())
	b = bin(num)[2:].zfill(32)
	b = flipBits(b)
	print(int(b,2))
