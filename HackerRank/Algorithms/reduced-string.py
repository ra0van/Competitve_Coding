#https://www.hackerrank.com/contests/101hack36/challenges/reduced-string
#AC
a = raw_input();
temp = a
prev = len(temp)
curr = 0
while prev!=curr:
	prev = len(a)
	for i in set(a):
		rep = i+i
		# print rep
		if rep in temp:
			temp = temp.replace(rep,'')
		a = temp
		curr = len(a)
if temp=='':
	print 'Empty String'
else:
	print temp