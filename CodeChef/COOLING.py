# https://www.codechef.com/problems/COOLING
# WA
t = int(raw_input())
while t:
	t -= 1
	n = int(raw_input())
	pie = map(int,raw_input().split())
	cool = map(int,raw_input().split())
	pie.sort(reverse=True)
	cool.sort(reverse=True)
	j = 0
	i = 0
	while j<n:
		if pie[i]<cool[j]:
			i += 1
			j += 1
			print pie[i],cool[j]
		else:
			j+=1

	print i
