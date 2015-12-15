# 
t = input()
for i in range(t):
	n = raw_input()
	n = float(n)
	print "Case "+str(i+1)+":",
	print "%0.2f "%(0.25 + (4*n*n))
