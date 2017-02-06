t = input()
for i in range(t):
	n = raw_input()
	a = map(int,raw_input().split())
	delay = [0]
	delayCount= 0
	fine  = 0
	for r in a:
		if r==0:
			fine += 1
			delay.append(delay[delayCount]+1)
			delayCount +=1
	print (fine*1000) + (delay[delayCount]*100)
	print fine,delay,delayCount
