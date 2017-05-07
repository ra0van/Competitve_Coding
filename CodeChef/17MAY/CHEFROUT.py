c,e,s = 0,1,2

t = input()
for _ in range(t):
	events = raw_input()
	ec,ee,es = 0,0,0
	impossible = False
	# print events
	for event in events:
		# print ec,ee,es
		if event == 'C':
			if ee >0 or es > 0:
				# print 'impossibe'
				impossible = True
				break
			ec+=1
		elif event == 'E':
			ee+=1
			if  es>0:
				impossible = True
				break
		elif event == 'S':
			es+=1
	if impossible :
		print 'no'
	else:
		print 'yes'