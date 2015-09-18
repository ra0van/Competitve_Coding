# https://www.hackerrank.com/challenges/pangrams

s = raw_input()
arr = [0]*26

for i in range(len(s)):
    tmp = ord(s[i])
    if s[i]!=' ':
        if tmp>=97 and tmp<=122:
            arr[tmp-97] = 1
        elif tmp>=65 and tmp<=90:
            arr[tmp-65] = 1


flag = False
i = 0
for i in range(26):
    if arr[i] == 0:
        flag = True
        break;
        
if flag:
    print "not pangram"
else:
    print "pangram"