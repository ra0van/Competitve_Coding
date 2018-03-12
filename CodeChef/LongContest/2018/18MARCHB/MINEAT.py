def compute(a,k):
    import math
    sum = 0
    for i in xrange(len(a)):
        sum += math.ceil((float(a[i]))/float(k))
    return sum
t =input()
while t>0:
    t-=1
    n,h = map(int,raw_input().split())
    arr = map(int,raw_input().split())
    arr.sort()
    start =1
    last = arr[n-1]
    for i in xrange(1,30):
        mid =(start+last)/2
        if compute(arr,mid)>h:
            start = mid+1
        else:
            last = mid
    print (start+last)/2
    