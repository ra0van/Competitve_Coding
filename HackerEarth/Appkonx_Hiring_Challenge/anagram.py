def isAnagram(a,b):
	count = [0]*256
	if len(a)!= len(b):
		return False
	
	for c1 in a:
		count[ord(c1)] += 1
	for c2 in b:
		count[ord(c2)] -= 1
	
	if max(count)!=0:
		return False
	else:
		return True


t = input()

for tc in range(t):
	a,b = raw_input().split()
	if isAnagram(a,b):
		print "YES"
	else:
		print "NO"