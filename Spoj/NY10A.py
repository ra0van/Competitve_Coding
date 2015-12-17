# your code goes here
t = input()
order = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH','HHT', 'HHH' ]
for i in range(t):
	n = input()
	s = raw_input()
	dic = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT' :0 , 'HHH':0 }
	print n,
	for i in range(0,38):
		dic[s[i:i+3]] += 1
	for k in order:
		print dic[k],
	print "\n"
	
