import sys
while  True:
	input = sys.stdin.readline()
	if input == '':
		break
	else:
		num = int(input)
		if num!=1:
			print (num-2)*2 + 2
		else:
			print 1