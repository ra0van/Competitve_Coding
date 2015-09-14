def mergeArray(a,b):
	if len(a)==0:
		return b
	if len(b) == 0:
		return a
	i,j,k =0,0,0
	c = []
	while i<len(a) and j<len(b):
		if a[i]<=b[j]:
			c.append(a[i])
			i += 1
			k += 1
		else:
			c.append(b[j])
			j += 1
			k += 1

	while i<len(a):
		c.append(a[i])
		i += 1
		k += 1
	while j<len(b):
		c.append(b[j])
		j += 1
		k += 1
	return c


n = int(raw_input())
arr = []
for i in range(n):
	tmpArr = map(int,raw_input().split())
	arr = mergeArray(arr,tmpArr)
	print arr