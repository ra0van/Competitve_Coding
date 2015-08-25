import sys

def getMin(arr,n):
	min = sys.maxint
	for i in range(n):
		if arr[i]<min and arr[i]>0:
			min = arr[i]

	return min

def checkZero(arr,n):
	count = False
	for i in range(n):
		if a[i]>0:
			count = True
	return count
n = int(raw_input())

a = map(int,raw_input().split(' '))

count = n
t = n
while count >1:
	if not checkZero(a,n):
		break;
	count = 0
	min = getMin(a,n)
	for i in range(n):
		if a[i]>0:
			a[i] = a[i]-min
			count += 1

	# for i in range(n):
	# 	print a[i],

	print count
