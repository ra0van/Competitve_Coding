#http://www.spoj.com/problems/ABCD/
n = input()
a = raw_input()
arr = []
brr = []

i = 0
while i<2*n:
	arr.append(a[i:i+2])
	i += 2
# print arr
for i in range(n):
	tmp =''
	for alp in 'ABCD':
		if alp not in arr[i]:
			# print alp,arr[i]
			tmp+=alp
	brr.append(tmp)
# print brr
for i in xrange(1,n):
	# print i,n,brr[i]
	if (brr[i][0]== brr[i-1][1]):
		brr[i] = brr[i][::-1]
tmp = ''
# print brr
for i in range(n):
	tmp += brr[i]
print tmp