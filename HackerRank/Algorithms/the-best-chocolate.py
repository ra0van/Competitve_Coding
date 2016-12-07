# https://www.hackerrank.com/contests/hour-of-code-2016/challenges/the-best-chocolate
fs,fp = map(int,raw_input().split())
ss,sp = map(int,raw_input().split())

f = fs/float(fp)
s = ss/float(sp)

if f>s:
    print "first"
elif s>f:
    print "second"
else:
    print "both"
