n = input()
a = map(int,raw_input().split())
if n<3:
    print 0
else:
    ins = max(a) - min(a)
    a1 = [i for i in a]
    a2 = [i for i in a]
    a1.remove(max(a))
    a2.remove(min(a))
    ins1 = max(a1)-min(a1)
    ins2 = max(a2) - min(a2)
    if ins1<ins2:
        print ins1
    else:
        print ins2