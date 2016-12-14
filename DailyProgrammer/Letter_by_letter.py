'''
Problem: https://www.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/
Challenge : 295 [Easy]
Change the a sentence to another sentence, letter by letter.
The sentences will always have the same length.

floor
bloor
broor
braor
brakr
brake


Bonus: made the char selection random and for input strings of different lengths
'''


import random
op = 'sherlock holmes'
ip = 'Matrix'

maxl = 0
diff = len(ip)-len(op)
if len(ip)>len(op):
	maxl = len(ip)
else:
	maxl = len(op)
if diff<0:
	ip = ' '*abs(diff) + ip
else:
	op = ' '*abs(diff) + op

mid = ip
print mid
ranger = [x for x in range(maxl)]
random.shuffle(ranger)
for i in ranger:
	if mid[i]!=op[i]:
		mid = list(mid)
		mid[i] = op[i]
		mid = ''.join(mid)
		print mid
	
