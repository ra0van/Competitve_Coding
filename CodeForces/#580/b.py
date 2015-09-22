n,d = map(int,raw_input().split())
li = []

for i in range(n):
	a = map(int,raw_input().split())
	li.append(a)

# li = sorted(li)

prev = li[0]
max_frnd_upto_here = li[0][1]
max_money_upto_here = li[0][0]

sum_upto_here = li[0][1]

for i in range(1,n):
	diff = max_money_upto_here-li[i][0]
	if diff<0:
		diff = abs(diff)
	if  diff > d:
		# print max_money_upto_here-li[i][0]
		if max_frnd_upto_here < sum_upto_here:
			max_frnd_upto_here = sum_upto_here
		if max_money_upto_here < li[i][0]:
			max_money_upto_here = li[i][0]
		sum_upto_here = li[i][1]
	else:
		sum_upto_here += li[i][1]
		max_money_upto_here = li[i][0]

if max_frnd_upto_here<sum_upto_here:
	max_frnd_upto_here = sum_upto_here

print max_frnd_upto_here

