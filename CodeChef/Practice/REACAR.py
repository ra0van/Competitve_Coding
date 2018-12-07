# https://www.codechef.com/problems/REACAR
# AC

def merge(left,right):
    result = []
    i,j,inversions = 0,0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            inversions += j
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    inversions += j*(len(left)-i)
    result += left[i:]
    result += right[j:]
    
    return inversions,result
    

def mergeSort(arr):
    if len(arr)<=1:
        return 0,arr
    mid = len(arr)/2
    leftInv,left = mergeSort(arr[:mid])
    rightInv,right = mergeSort(arr[mid:])
    mergeInv,merged = merge(left,right)
    return leftInv+rightInv+mergeInv, merged

def main():
    n = input()
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    ind = []
    for i in a:
        k = b.index(i)
        ind.append(k)
    inv, merged = mergeSort(ind)
    print(inv)

if __name__ == '__main__':
    main()