#wa, partial
t = input()
for _ in xrange(t):
  s = raw_input()
  start = 1
  num = [start]
  prev = start
  for i in s:
    if i=='>':
      num.append(prev-1)
      prev -=1
    elif i=='=':
      num.append(prev)
    elif i=='<':
      num.append(prev+1)
      prev += 1
  # print num
  m = min(num)
  print max(num) - m +1 
    
    
