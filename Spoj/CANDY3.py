t = int(raw_input())
raw_input()

while t:
	t-=1
	sum=0
	count=0
	a = []
	while 1:
		try:
			tmp = int(raw_input())
			a.append(tmp)
			count +=1
		except:
			if sum%count == 0:
				print("YES")
			else:
				print("NO")
			break;

