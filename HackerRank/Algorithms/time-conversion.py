# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/time-conversion
s = raw_input().split(':')
ap = s[2][2:]
s[2] = s[2][:2]
if (ap=='AM' and s[0]!='12') or (ap=='PM' and s[0]=='12'):
    print s[0]+':'+s[1]+':'+s[2]
elif ap=='PM' and s[0]!='12':
        print str(int(s[0])+12) + ':' + s[1] + ':' +s[2]
elif ap=='AM' and s[0]=='12':
    print '00:' + s[1] + ':' +s[2]

    
    