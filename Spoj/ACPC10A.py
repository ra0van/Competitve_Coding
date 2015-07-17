while 1:
	a,b,c = raw_input().split(' ')
	a=int(a)
	b=int(b)
	c=int(c)

	if a==0 and b==0 and c==0:
		break;
	
	v1 = b-a
	v2 = c-b
	if v1==v2:
		print("AP " + str(c+v1))		
	else:
		v1 = b/a
		print("GP " + str(c*v1))