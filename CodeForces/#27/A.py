n=input()
a = map(int,raw_input().split())
a.sort()
first = a[:n]
second = a[n:]
if min(second) > max(first):
    print 'YES'
else:
    print 'NO'