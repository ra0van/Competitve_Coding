t = int(raw_input())

while t:
	s=raw_input()
	t-=1

	n = int(raw_input())
	sum=0
	for i in xrange(n) :
		sum = sum+int(raw_input())

	if sum%n==0 :
		print("YES");
	else:
		print("NO");

