def f(n):
	# print 'in'
	if n not in val:
		val[n] = max(n,f(n/2)+f(n/3)+f(n/4))
	return val[n]

val = {}
val[0] = 0
val[1] = 1
val[2] = 2
val[3] = 3

isValid = True
while isValid:
	try:
		line = input()
		num = int(line)
		if num not in val:
			val[num] = max(num,f(num/2)+f(num/3)+f(num/4))
			print val[num]
		else:
			print val[num]
	except:
		isValid = False
