def try_reduce(string):
	a_count = 0
	b_count = 0
	c_count = 0

	for i in range(len(string)):
		if string[i]=='a':
			a_count += 1
		elif string[i]=='b':
			b_count += 1
		elif string[i]=='c':
			c_count += 1

	if (a_count == 0 and b_count == 0 ) or (a_count == 0 and c_count == 0 )  or (c_count == 0 and b_count == 0 ) :
		return len(string)
	elif (a_count%2 == b_count%2== c_count%2 ):
		return 2;
	else :
		return 1;
	


t = int(raw_input())


while t:
	t -= 1
	s = raw_input()
	print(try_reduce(s))