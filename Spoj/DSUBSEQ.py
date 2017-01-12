#www.spoj.com/problems/DSUBSEQ
#TLE on testcase 2
from sys import stdin,stdout

def FindCount(s):
	MAX_CHAR = 26
	last = [-1]*MAX_CHAR
	#print len(s)+1
	dp = [0]*(len(s)+1)
	dp[0] = 1
	for i in xrange(1,len(s)+1):
		dp [i] = 2*dp[i-1]
		
		if last[ord(s[i-1])-65] !=-1:
			dp[i] = dp[i]-dp[last[ord(s[i-1])-65]]
			if dp[i]<0:
				dp[i]=1
		last[ord(s[i-1])-65] = i-1
	#print dp
	return str(dp[len(s)]%1000000007)
	
n = int(stdin.readline().strip())
lines = stdin.readlines()
for line in lines:
	q = line.strip()
	#q = ['a']*100000
	stdout.write(FindCount(q)+'\n')
