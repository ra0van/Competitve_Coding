t = input()
for i in range(t):
	n = raw_input()
	a = map(int,raw_input().split())
	track= [] 
	trackb= []
	trackCount = 1
	prev = -1
	fine  = 1 if a[0]==1 else 0
	for r in a:
		if r==0:
			fine += 1
		if prev==r:
			trackCount +=1 
		else:
			track.append(trackCount)
			trackb.append(r)
			prevCount = 1
			prev = r

