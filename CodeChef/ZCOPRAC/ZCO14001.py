def main():
  n,h = map(int,raw_input().split())
  box = map(int,raw_input().split())
  command = map(int,raw_input().split())
  
  currpos = 0
  picked = False
  for i in command:
    if i == 0: 
      break
    elif i == 1:
    	if currpos>0 and currpos<n:
    		currpos-=1
    elif i == 2:
    	if currpos>-1 and currpos<n-1:
    		currpos+=1
    elif i==3:
    	if currpos>=0 and currpos <n and picked == False:
    	  if box[currpos]>0:
    		  box[currpos] -= 1
    		  picked = True
    elif i==4:
    	if currpos>=0 and currpos <n and picked == True and box[currpos]<h:
    		box[currpos] += 1
    		picked = False
  for i in box:
    print i,
  print "\n"
if __name__ == '__main__':
  main()