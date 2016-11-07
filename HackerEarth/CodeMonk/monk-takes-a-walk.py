#https://www.hackerearth.com/codemonk-searching/algorithm/monk-takes-a-walk/

n = input()
a = 'aeiouAEIOU'

for i in range(n):
	tree = raw_input()
	bad = 0
	
	for j in tree:
		for k in a:
			if j==k:
				bad+=1
				break

	print bad
