# https://www.codechef.com/problems/MAXCOUNT

t = int(raw_input())

while t:
	t -= 1
	n = int(raw_input())
	a = map(int,raw_input().split())
	a.sort()
	val = a[0]
	count = 1
	prev = a[0]
	curr_count = 0
	i = 0
	# print a
	while i<n:
		if prev==a[i]:
			curr_count+=1
			# print curr_count
		else:
			if curr_count>count:
				count = curr_count
				val = prev
				curr_count = 1
				prev = a[i]
			else:
				prev = a[i]
				curr_count = 1
		i += 1
	if curr_count>count:
		count = curr_count
		val = prev
	print val,count