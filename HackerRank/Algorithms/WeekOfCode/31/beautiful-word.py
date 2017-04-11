://www.hackerrank.com/contests/w31/challenges/beautiful-word
import sys

s = raw_input()
vowels = 'aeiouy'
prev = ''
beauty = True
for i in s:
    if prev == i:
        beauty=False
        #print i,prev
        break
    if i in vowels and prev in vowels and prev!='':
        beauty=False
        #print i,prev,'v'
        break
    prev = i
if beauty:
    print 'Yes'
else:
    print 'No'

