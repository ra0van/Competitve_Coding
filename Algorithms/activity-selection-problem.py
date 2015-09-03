#http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/

def MaxActivity(s,f):
	i,j=0,1
	print i,
	for j in xrange(1,len(s)):
		if s[j]>=f[i]:
			print j,
			i = j

start  = [1,3,0,5,8,5]
finish = [2,4,6,7,9,9]

MaxActivity(start,finish);