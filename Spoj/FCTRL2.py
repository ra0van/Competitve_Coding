def fact(num):
	if num<=0:
		return 1;
	return num*fact(num-1);

t = int(input());
while t>0:
	t-=1;
	n = int(input());
	#n= fact(n);
	print(fact(n));