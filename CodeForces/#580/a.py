#http://codeforces.com/contest/580/problem/A

n = input()
a = map(int,raw_input().split())

curr_seq = 1
max_seq = 0

prev = a[0]
for i in range(1,n):
	if a[i]>=prev:
		curr_seq+=1
	else:
		if curr_seq>max_seq:
			max_seq = curr_seq
		curr_seq=1
	prev = a[i]
if curr_seq>max_seq:
	max_seq = curr_seq
print max_seq