# https://www.codechef.com/APRIL17/problems/SIMDISH
# AC
n = input()
yes='similar'
no='dissimilar'
for i in range(n):
	a = map(str,raw_input().split())
	b = map(str,raw_input().split())
	a.sort()
	b.sort()
	count = 0
	for e in a:
		if e in b:
			count+=1
		if count==2:
			break;
	if count==2:
		print yes
	else:
		print no
