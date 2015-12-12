import sys
t= input()
for i in range(t):
	line = sys.stdin.readline()
	lefts,rights = map(str,raw_input().split('='))
	left = lefts.strip()
	right = rights.strip()
	x,y = map(str,left.split('+'))
	x = x.strip()
	y = y.strip()
	# print str(x.isdigit())+x+"a"
	# print str(y.isdigit())+y+"b"
	# print str(right.isdigit())+right+"r"

	if x.isdigit()==False:
		num = int(right)-int(y)
		print str(num)+" + "+y+" = "+right
	elif y.isdigit()==False:
		num = int(right)-int(x)
		print x+" + "+str(num)+" = "+right
	elif right.isdigit()==False:
		num = int(y)+int(x)
		print x+" + "+y+" = "+str(num)
	else:
		print lefts+"="+rights
