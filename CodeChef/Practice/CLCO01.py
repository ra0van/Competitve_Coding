#https://www.codechef.com/problems/CLCO01

def main():
    #loop for test
    for x in xrange(input()):
        cmd_stack=[]
        #loop for n
        for y in xrange(input()):
            cmd=map(str, raw_input().split())
    
            if cmd[0]=='pwd':
                dir=''
                for val in cmd_stack:
                    dir = dir+'/'+val
                print dir+'/'
            
            elif(cmd[1][0])=='/':
                cmd_stack=[]
                new_dir = cmd[1].split('/')
    
                for val in new_dir:
                    if len(val)!=0 and val!='..':
                        cmd_stack.append(val)
                    if val=='..':
                        cmd_stack.pop() 
    
            else:
                new_dir = cmd[1].split('/')
                for val in new_dir:
                    if len(val)!=0 and val!='..':
                        cmd_stack.append(val)
                    if val=='..':
                        cmd_stack.pop()
                
            

            
            
if __name__ == '__main__':
    main()