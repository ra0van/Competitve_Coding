def removeDuplicates(arr):
	arr = list(set(arr))
	return sorted(arr)
	

t = input()
for i in range(t):
	a = map(int,raw_input().split())
	a = a[1:]
	b = map(int,raw_input().split())
	b = b[1:]
	a = removeDuplicates(a)
	b = removeDuplicates(b)
	a_len = len(a)
	b_len = len(b)
	min_diff = max(max(a),max(b))
	i = 0
	j = 0
	while (i<a_len) and (j<b_len):
		diff = abs(a[i]-b[j])
		if diff < min_diff:
			min_diff = diff
		
		if a[i]<b[j]:
			i += 1
		else:
			j += 1
			
	print min_diff
	
