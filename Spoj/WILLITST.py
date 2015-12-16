# your code goes here
n = input()
a = [n]
flag = False
while n>1:
	if n%2==0:
		n = n/2
	else:
		n = 3*n+3
	
	if n in a:
		flag = True
		break;
	else:
		a.append(n);

if flag:
	print "NIE";
else:
	print "TAK"
	
