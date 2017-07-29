#https://www.codechef.com/FEB16/problems/CHEFDETE
import sys
n = int(raw_input())
a = map(int,sys.stdin.readline().split(' '))
li = [0]*(n+1)
for i in a:
	li[i] += 1
isComplete = False
suspect = []
# print li
while True:
	if isComplete:
		break;
	s = min(li)
	# print s
	if s==0:
		suspect.append(li.index(s))
		li[li.index(s)] = 1
	else:
		isComplete =  True

suspect = sorted(suspect)
for s in suspect:
	print s,
