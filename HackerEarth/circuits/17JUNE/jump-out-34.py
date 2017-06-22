def main():
	n = input()
	a = map(int,raw_input().split())
	pos = -1
	for i in xrange(n):
		jump = a[i]
		if i+jump >n-1:
			pos = i+1
			break
	print pos

if __name__ == '__main__':
	main()