#https://www.codechef.com/SEPT15/problems/MSTEP

def find(a,val,n):
	for i in range(n):
		if val in a[i]:
			return i,a[i].index(val)
x=-1
y=-1
t = int(raw_input())
while t:
	t -= 1
	n = int(raw_input())
	a = [[-1]*n]*n
	for i in range(n):
		a[i] = map(int,raw_input().split())

	count = 0
	currx=-1
	curry=-1
	for i in range(n*n):
		x,y = find(a,i+1,n)
		if i==0:
			currx = x
			curry = y
		else:
			count += abs(currx-x)
			count += abs(curry-y)
			currx = x
			curry = y
	print count
