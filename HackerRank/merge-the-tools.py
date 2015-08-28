
def removeRepeats(s):
	chArr = [0]*26
	for i range(len(s)):
		

ip = raw_input()
k = int(raw_input())

a = [ip[i:i+k] for i in range(0,len(ip),k)]

for i in range(len(a)):
	removeRepeats(a[i])