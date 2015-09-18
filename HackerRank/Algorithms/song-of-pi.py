pi =  '31415926535897932384626433833'
yes = "It's a pi song."
no = "It's not a pi song."

t = int(raw_input())

while t:
	t -= 1
	s = raw_input().split(' ')
	l = len(s)

	piStr = ''
	for i in range(l):
		piStr += str(len(s[i]))

		

	if piStr == pi[:len(piStr)] :
		print yes
	else:
		print no


