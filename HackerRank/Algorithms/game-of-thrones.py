s = raw_input()
l = len(s)
a = [0 for i in range(26)]

odd_count =0

for i in range(l):
	num = ord(s[i])-97
	a[num] += 1

for i in range(26):
	if a[i]%2 ==1:
		odd_count += 1

if odd_count > 1:
	print "NO"
else:
	if l%2==1 and odd_count==1:
		print "YES"
	elif l%2==0 and odd_count==0:
		print "YES"
	else:
		print "NO"
	

