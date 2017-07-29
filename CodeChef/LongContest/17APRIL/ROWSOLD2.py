def next_movable_1(string):
  one = -1
  for i in range(len(string)):
    x = string[i]
    if x=='1':
      one = i
    else:#0 case
      if one>-1: #encountered 0 right after a 1
        return one
  return -1
  
n = int(input());
for i in range(n):
  input = map(str,raw_input().strip())
  pos = next_movable_1(input)
  #print input;
  #print pos
  count = 0
  while  pos!= -1:
    count +=1
    idx = pos
    while idx<len(input):
      if idx==len(input)-1:
        break
      if input[idx+1]=='1' :
          break
      
      input[idx],input[idx+1] = input[idx+1],input[idx]
      #print input
      count +=1
      idx+=1
    pos = next_movable_1(input)
    #print pos
  print count
