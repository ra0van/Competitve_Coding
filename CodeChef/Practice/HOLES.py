# https://www.codechef.com/problems/HOLES

t =  int(raw_input())
arr = [1,2,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0]
while t:
	t -= 1
	count = 0
	s = raw_input()
	for i in range(len(s)):
		val = ord(s[i])-65
		count += arr[val]
	print count
