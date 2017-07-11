#AC
t = input()
for _ in xrange(t):
  s = raw_input()
  max_l,curr_l = 0,0
  max_g,curr_g = 0,0
  
  for i in s:
    if i=='>':
      curr_g += 1
      if curr_g>max_g:
        max_g = curr_g
      curr_l = 0
    elif i =='<':
      curr_l += 1
      if curr_l > max_l:
        max_l = curr_l
      curr_g = 0
    
  if curr_l > max_l:
      max_l = curr_l
  
  if curr_g>max_g:
      max_g = curr_g
      
  if max_g>max_l:
    print max_g + 1
  else:
    print max_l + 1
