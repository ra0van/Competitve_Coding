def hasCommonChars(s1,s2):
	return len(set(s1) & set(s2))>0

def main():
	t = input()
	for c in range(t):
		a = raw_input()
		b = raw_input()
		if hasCommonChars(a,b):
			print "Yes"
		else:
			print "No"


if __name__ == "__main__":
	main()