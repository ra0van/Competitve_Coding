

t = input()

for c in range(t):
	a,b,c = map(int,raw_input().split())
	ans = 0
	for i in range(3):
		arem = a-i
		brem = b-i
		crem = c-i
		
		if (arem<0 or brem<0 or crem<0):
			continue
		ans = max(ans, i+arem/3+brem/3+crem/3)
		
	print ans