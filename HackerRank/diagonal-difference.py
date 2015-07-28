
def getSumLtoR(a,l):
	sum = 0
	pos = 0
	for i in range(l):
		sum += a[i][pos]
		pos += 1

	return sum

def getSumRtoL(a,l):
	sum = 0
	pos = l-1
	for i in range(l):
		sum += a[i][pos]
		pos -= 1
	return sum

def mod(num):
	if num<0:
		return num*(-1)
	return num

n = int(raw_input())

arr = [[0 for x in range(n)]  for x in range(n)]

for x in range(n):
	arr[x] = map(int,raw_input().split(' '))
	
sum1 = getSumLtoR(arr,n)
sum2 = getSumRtoL(arr,n)

print(mod(sum1-sum2))