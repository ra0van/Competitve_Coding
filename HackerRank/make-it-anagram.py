# https://www.hackerrank.com/challenges/make-it-anagram

a = raw_input()
b = raw_input()

st = [0]*26
count = 0
if a == b:
    print count
else:
    for i in range(len(a)):
        tmp = ord(a[i])
        st[tmp-97] += 1
    for i in range(len(b)):
        tmp = ord(b[i])
        st[tmp-97] -= 1
    

    for i in range(26):
        if st[i]!=0:
            if st[i]<0:
                count += (st[i]*-1)
            else:
                count += st[i]
                
    print count
            