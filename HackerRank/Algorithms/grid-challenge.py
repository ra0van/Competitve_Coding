# https://www.hackerrank.com/challenges/grid-challenge
# partial
# 18.8/20
def isSort(arr,n):
	for i in range(n-1):
		if arr[i]>arr[i+1]:
			return False;
	return True;

t = input()
for i in range(t):
	n = input()
	a = []
	for i in range(n):
		a.append(sorted(raw_input()))
	tmp = zip(*a[::-1])
	rt = []
	for t in tmp:
		rt.append(t[::-1])

	flag = isSort(a,n)
	flagF = isSort(rt,n)

	if flag==True and flagF==True:
		print "YES"
	else:
		print "NO"

	