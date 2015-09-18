n = int(raw_input())

a = [0 for i in range(26)]
t = n
while t:
	t -= 1;
	s = raw_input()
	
	s = ''.join(sorted(s))
	
	prev = ''

	for i in range(len(s)):
		if s[i]!=prev:
			num = ord(s[i])-97
			#print num
			a[num] += 1
			prev = s[i]

count =0
for i in range(26):
		if a[i]==n:
			count += 1
print count