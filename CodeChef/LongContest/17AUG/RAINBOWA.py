yes = 'yes'
no = 'no'

t = input()
for _ in xrange(t):
    n = input()
    a = map(int,raw_input().split())
    start,end = 0,n-1
    s = sum(set(a))
    if(s!=28):
        print no
    else:
        prev = 1
        flag = True
        while start<end:
            if a[start]==a[end] :
                if a[start]-prev > 1:
                    flag = False
                    break
                start += 1
                end -= 1
                prev = a[start]
            else:
                flag=False
                break
        if flag:
            print yes
        else:
            print no