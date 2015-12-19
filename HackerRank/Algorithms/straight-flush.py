#https://www.hackerrank.com/contests/101hack32/challenges/straight-flush
def main():
	n = [-1]*5
	s = [-1]*5
	order = ['2','3','4','5','6','7','8','9','T','J','Q','K']
	a_index = -1
	for i in range(5):
		# print n[i],s[i]
		temp  = raw_input()

		n[i] = temp[0]
		s[i] = temp[1]
		if n[i]=='A':
			a_index = i
	Suite = True
	for i in range(4):
		if s[0]!=s[i]:
			Suite = False
			break

	if Suite == False:
		print "NO"
		return

	dup = True
	for i in n:
		if n.count(i)>1:
			print i
			dup=False
			break

	if dup==False:
		print "NO"
		return

	popped = False
	if a_index >=0 and a_index<=4:
		popped = True
		n.pop(a_index)

	ind = [-1]*len(n)
	for i in range(len(n)):
		ind[i]=order.index(n[i])

	ind  = sorted(ind)
	seq = True
	for i in range(len(ind)-1):
		if ind[i]-ind[i+1]!=-1:
			# print ind[i]
			seq = False
			break;
	# print ind
	if seq==False:
		print"NO"
		return

	seq = True
	if popped==True:
		if 'K' in n or '2' in n:
			seq = True
		else:
			seq = False
	if seq==True:
		print 'YES'
	else:
		print 'NO'






if __name__ == '__main__':
	main()