#AC
n = int(input());

for i in xrange(n):
  input = raw_input().strip()
  l = len(input)
  dp = [0]
  count = 0
  j = 0
  for k in xrange(l-1,-1,-1):
    x = input[k]
    if x=='1':
      steps = dp[j]+count
      if count>0:
        steps+=1
      dp.append(steps)
      count =0
      j+=1
    else:
      count +=1
  print sum(dp)
