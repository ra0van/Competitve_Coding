def deli(a,k):
    total = 0
    rsum = sum(a[1:])
    if rsum%k ==0:
        total = 1
    
    if len(a) <=2 :
        return total
    
    total += deli(a[:-1],k)
    total += deli(a[1:],k)
    return total


def main():
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    a.sort()
    count = deli(a,k)
    print count
    
if __name__ == '__main__':
    main()