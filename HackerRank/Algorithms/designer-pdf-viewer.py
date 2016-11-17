#https://www.hackerrank.com/contests/101hack40/challenges/designer-pdf-viewer
#AC
a = map(int,raw_input().split())
r = raw_input()

l = len(r)
max_h = -1
for ele in r:
	h = a[ord(ele)-97]
	if h > max_h:
		max_h  = h 

print l*max_h