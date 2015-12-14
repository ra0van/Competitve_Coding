n = raw_input()
num = n
count = 0
li = {}
flag = True
while num!='1':
	sum = 0
	for i in num:
		sum += int(i)**2
	num = str(sum)
	count += 1
	if sum in li:
		flag = False
		break
	else:
		li[sum] = 1
if flag:
	print count
else:
	print -1
