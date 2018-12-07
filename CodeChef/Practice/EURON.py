def merge(arr,p,q,r):
    l1 = q-p+1
    l2 = r-q
    L,R = [],[]
    for i in xrange(p,q+1):
        L.append(arr[i])
    for i in xrange(q+1,r+1):
        R.append(arr[i])
    v = 0
    i,j = 0,0
    
    k = p
    while i<l1 and j<l2:
        if L[i]<=R[j]:
           arr[k] = L[i]
           i += 1
        else:
            arr[k] = R[j]
            v += l1-i
            j += 1
        k += 1
    while i<l1 and k<=r:
        arr[k] = L[i]
        k += 1
        i += 1
    
    while j<l2 and k<=r:
        arr[k] = R[j]
        k += 1
        j += 1
    
    return v
    

def mergeSort(arr,p,r):
    k = 0
    if p<r:
        q = abs((p+r)/2)
        k += mergeSort(arr,p,q)
        k += mergeSort(arr,q+1,r)
        k += merge(arr,p,q,r)
    return k

def main():
    n = input()
    a = map(int,raw_input().split())
    print(mergeSort(a,0,n-1))

if __name__ == '__main__':
    main()