# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b,n = map(int,raw_input().split(' '))

arr = [0]*n

arr[0] = a
arr[1] = b

for i in range(n):
	if i==0 or i == 1:
		pass
	else:
		arr[i] = (arr[i-1]**2)+arr[i-2]

print arr[n-1]
