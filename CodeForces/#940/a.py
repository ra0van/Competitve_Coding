n,d = map(int,raw_input().split())
a = map(int,raw_input().split())
a.sort()
max_d = a[n-1] - a[0]
count = 0
l = n
while(max_d > d):
    a = a[:l-1]
    l = l-1
    max_d = a[l-1]-a[0]
    count += 1
    
print count