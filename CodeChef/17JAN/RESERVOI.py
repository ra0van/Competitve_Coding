from sys import stdin,stdout


t = int(stdin.readline().strip())
for l in xrange(t):
	n,m = map(int,stdin.readline().strip().split())
	r = []
	for i in xrange(n):
		x = stdin.readline().strip()
		#print x,list(x)
		r.append(list(x))
	unstable = False
	#print r
	for i in xrange(n):
		if unstable:
			break;
		for j in xrange(m):
			if unstable:
				break;
			if  r[i][j]=='B':
				#base should be B
				#sides can be A/W
				if i+1<n: # base
					if r[i+1][j]!='B':
						unstable=True
						break;
			elif r[i][j] == 'W':
				#all sides should be brick
				#top should be air 
				if j==0 or j-1==m or i==n-1:
					unstable = True
					break;
				if i+1<n: #base
					if r[i+1][j]=='A':
						unstable=True
						break
				if i-1>=0:#top should be air
					if r[i-1][j]=='B':
						unstable=True
						break;
				if j+1<m:# right side should be brick
					if r[i][j+1]=='A':
							unstable = True
							break;
				if j-1>=0:#left side should be brick
					if r[i][j-1]=='A':
							unstable = True
							break;
			elif r[i][j]=='A':
				#bottom can be brick or water
				#if i+1<n:#bottom
					# if r[i+1][j]=='A':
					# 	unstable = True
					# 	break;
				if i-1>=0:#top
					if r[i-1][j]!='A':
						unstable = True
						break;
				if j-1>=0:#left
					#print r[i][j-1]
					if r[i][j-1]=='W':
						unstable=True
						break
				if j+1<m:
					#print r[i][j+1]
					if r[i][j+1]=='W':
						unstable= True
						break
			
					
	if unstable:
		print 'no'
	else:
		print 'yes'
	
	
