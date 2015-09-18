# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())

a = map(int,raw_input().split(' '))
sum =0
for i in xrange(t):
	sum += a[i]

print(sum)