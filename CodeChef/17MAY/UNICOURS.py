t = input()
for _ in range(t):
	n = input()
	c = map(int,raw_input().split())
	dp = [1]
	used = 1
	for i in range(1,n):
		rem = i-c[i]
		used = max(c[i],used)
		if rem==0:
		  dp.append(1)
		else:
		  dp.append(i+1-used)
		
	print dp[n-1]
