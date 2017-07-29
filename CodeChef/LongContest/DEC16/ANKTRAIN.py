# your code goes here
#Partial (50%)
def print_pair(seat):
	if seat ==1:
		print "4LB"
	elif seat ==2:
		print "5MB"
	elif seat ==3:
		print "6UB"
	elif seat==4:
		print "1LB"
	elif seat==5:
		print "2MB"
	elif seat==6:
		print "3UB"
	elif seat==7:
		print "8SU"
	elif seat==0:
		print "7SL"

t = input()
for i in xrange(t):
	q = input()
	rem = q%8
	print_pair(rem)
