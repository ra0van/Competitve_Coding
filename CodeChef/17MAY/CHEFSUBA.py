def rotate(a,n):
  return a[n:] + a[:n]
 
def getMax(a,k,n):
  k = min(k,n)
  m,c = 0,0
  for i in range(n-k+1):
    c = a[i:i+k].count(1)
    if c>m:
      m=c
  return m
 
n,k,p = map(int,raw_input().split())
a = map(int,raw_input().split())
q = raw_input()
 
 
prev = ''
count = 0
qcount = 0
i = 0
while i<p:
  if q[i]=='?':
	qcount = 1
	while i+1<p:
		if(q[i+1]=='?'):
			qcount += 1
			i+=1
		else:
			break
	if k>n:
		ans = a.count(1)
	else:
		ans = getMax(a,k,n)
	# print qcount,"as"
	for _ in range(qcount):
		print ans
  else:
    count = 1
    while i+1<p:
      if(q[i+1]=='!'):
        count += 1
        i+=1
      else:
        break
    # print count
    a = rotate(a,-count)
  i+=1 
