#WA
t = input()
for i in range(t):
	s = raw_input()
	ch = ''
	for st in s:
		if st.isdigit() == False:
			ch = st

	a,b = s.split(ch)

	if ch=='+':
		plus = int(a)+int(b)
		off = max(len(a),len(b)+1)
		print (off-len(a))*' '+a
		print (off-len(b)-1)*' '+ch+b
		print off*'-'
		print (off-len(str(plus)))*' '+str(plus)
	elif ch=='-':
		sub = int(a)-int(b)
		off = max(len(a),len(b)+1)
		print (off-len(a))*' '+a
		print (off-len(b)-1)*' '+ch+b
		print off*'-'
		print (off-len(str(sub)))*' '+str(sub)
	elif ch=='*':
		val = []
		for st in b:
			val.append(int(a)*int(st))
		val = val[::-1]
		final = int(a)*int(b)
		l= [len(str(i)) for i in val]
		l.append(len(a))
		l.append(len(b)+1)
		l.append(len(str(final)))
		off = max(l)
		# print off
		print (off-len(a))*' '+a
		print (off-len(b)-1)*' '+ch+b
		j = 0
		if len(val)>1:
			print max(len(a),len(b)+1)*'-'
			for v in val:
				print (off-j-len(str(v)))*' '+str(v)+j*' '
				j += 1
		print (off-1)*'-'
		print (off-len(str(final)))*' '+str(final)




