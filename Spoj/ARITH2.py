# your code goes here
t =input()

for i in range(t):
	raw_input()
	s = raw_input()

	# s = s.rstrip('=')
	s = s.strip()
	s = s.replace(' ','')
	num = []
	op = []
	temp = ''
	for i in s:
		#print i
		if i.isdigit():
			temp += i
		else:
			num.append(int(temp))
			temp = ''
			op.append(i)
	val = num[0]
	#print num,op
	for i in range(len(op)):
		if op[i]=='+':
			val += num[i+1]
		elif op[i] == '-':
			val -= num[i+1]
		elif op[i] == '*':
			val *= num[i+1]
		elif op[i] == '/':
			val /= num[i+1]
		elif op[i] == '=':
			break
	
	print val
		
