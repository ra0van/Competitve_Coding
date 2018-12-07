def mergeSort(l,r,i,stack):
    if i < l or i > r:
        return 
    mid = (r-l)/2
    stack += 1
    if l==r== i:
        print l,r
        print stack
        return
        
    if i <= l+mid:
        print l,r
        mergeSort(l,l+mid,i,stack)
    elif i > l+mid:
        print l,r
        mergeSort(l+mid+1,r,i,stack)
        
    return

def main():
    t = input()
    for _ in xrange(t):
        l,r,i = map(int,raw_input().split())
        if i < l or i > r:
            print -1
        mergeSort(l,r,i,0)

if __name__ == '__main__':
    main()