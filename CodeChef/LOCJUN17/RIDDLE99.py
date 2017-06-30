#https://www.codechef.com/LOCJUN17/problems/RIDDLE99
t = input()
for _ in xrange(t):
  a,b,m = map(int,raw_input().split())
  count = 0
  start = a/m
  if a%m!=0:
    start += 1
  end = b/m
  count = end-start+1
  print count
    
