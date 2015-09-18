# incomplete
s = raw_input();
l = len(s);
a = [0]*26;
sr = {}
for i in range(l):
	tmp = ord(s[i])-97;
	a[tmp] += 1

for i in range(25,-1,-1):
	if a[i]>0:
		sr[chr(i+97)] = a[i]

# print(sorted([value,key] for (key,value) in sr.items()))
a = sorted([value,key] for (key,value) in sr.items());
l = len(a)
print a
for i in range(l-1,-1,-1):
	tmp = a[i];
	if tmp[0]>0:
		print tmp[1],str(tmp[0])
	
