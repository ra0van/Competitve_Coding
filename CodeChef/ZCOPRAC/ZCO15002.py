def main():
	n,k = map(int,raw_input().split())
	a = map(int,raw_input().split())
	a.sort()
	count = 0
	for i in xrange(n):
		for j in xrange(i+1,n):
			if a[j]-a[i] >=k:
				count += n-1-j
				break
	print count

if __name__ == '__main__':
	main()