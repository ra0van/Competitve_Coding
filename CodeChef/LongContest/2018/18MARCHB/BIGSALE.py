t = input()
while t>0:
    t-=1
    n = input()
    totalLoss = 0
    for i in xrange(n):
        price,q,discount = map(int,raw_input().split())
        price_d = price*(1-(discount/100.0))
        price_i = price_d*(1+(discount/100.0))
        loss = price-price_i
        totalLoss += loss*q
    print totalLoss