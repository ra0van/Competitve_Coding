t = int(raw_input())
string = "hackerrank"
l = len(string)
while t:
	t -= 1
	s = raw_input()
	
	if s[:l]==string and s[-l:] == string:
		print 0
	elif s[:l]==string:
		print 1
	elif s[-l:]==string:
		print 2
	else:
		print -1
	