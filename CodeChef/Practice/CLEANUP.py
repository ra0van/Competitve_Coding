# https://www.codechef.com/problems/CLEANUP
t = int(raw_input())

while t:
	n,m = map(int,raw_input().split())
	a = map(int,raw_input().split())

	act = [0]*(n+1)

	for i in range(m):
		tmp = a[i]
		act[tmp] = 1
	flag = True
	for i in range(n+1):
		if act[i]==0 and i!=0:
			if flag:
				print i,
				act[i] = 1
			flag = not flag
	print ''
	for i in range(n+1):
		if act[i]==0 and i!=0:
			print i,
	print ''
	t -=1 