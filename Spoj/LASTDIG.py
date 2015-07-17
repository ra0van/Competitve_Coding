t =int(raw_input())
while t:
	t-=1
	a,b= raw_input().split()
	a=int(a)
	b=int(b)

	if b==0 or a==0:
		print(1)
	else:
		rem = b%4
		print((a**rem)%10)
		
