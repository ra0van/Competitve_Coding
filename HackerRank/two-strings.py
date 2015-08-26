#https://www.hackerrank.com/challenges/two-strings
t = int(raw_input())

while t:
    t -= 1
    a = raw_input()
    b = raw_input()
    
    s = [-1]*26
    flag = False
    
    for i in range(len(a)):
        tmp = ord(a[i])-97
        s[tmp] = 0
    
    for i in range(len(b)):
        tmp = ord(b[i]) - 97
        if s[tmp] == 0:
            flag = True
            break
            
    if flag:
        print "YES"
    else:
        print "NO"