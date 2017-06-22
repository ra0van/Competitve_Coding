def main():
	n,k = map(int,raw_input().split())
	a = map(int,raw_input().split())
	a.sort()
	count = 0
	m = max(a)
	prev = -1
	prev_count = 0
  	for i in xrange(n):
	    if a[i]==prev:
	    	count += prev_count
	    	continue
	    if m-a[i] < k :
	    	prev_count = 0
	    	prev = a[i]
	    	continue
	   	prev_count = 0
	    for j in xrange(i+1,n):
	      if a[j]-a[i] >=k:
	        count += n-j
	        prev_count = n-j
	        break
	   	prev = a[i]
	print count

if __name__ == '__main__':
	main()