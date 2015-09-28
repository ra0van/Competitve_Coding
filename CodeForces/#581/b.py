# http://codeforces.com/contest/581/problem/B
# TLE
n = input()
a = map(int,raw_input().split())

for i in range(n-1):
	print max(max(a[i+1:])-a[i]+1,0),
print 0
