# https://www.hackerrank.com/challenges/sherlock-and-array


t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    a = map(int,raw_input().split(' '))
    left = 0 
    right = 0
    for i in range(n):
        right += a[i]
    pos = 0
    flag = False
    for i in range(n):
        if right == left:
            flag = True
            break;
        else:
            if i<n:
                right -= a[i]
            if i>0:
                left += a[i-1]
                
            if right == left:
                flag = True
                break;
                
                
    if flag:
        print "YES"
    else:
        print "NO"
            
