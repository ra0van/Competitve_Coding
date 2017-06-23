def main():
	n,k = map(int,raw_input().split())
	a = map(int,raw_input().split())
	a.sort()
	count  = 0
	l,r = 0,n-1
	
	while l<r:
	  if a[l] + a[r] < k:
	    count += (r-l)
	    l += 1
	  else:
	    r -= 1
	
	print count

if __name__ == '__main__':
	main()
