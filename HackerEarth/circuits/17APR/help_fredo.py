#TLE
import math
import operator


n = input()
a = map(int,raw_input().split())
prod = 1
#for i in a:
#	prod *= i

prod = reduce(operator.mul,a,1)

#print prod
print int(math.ceil(prod**(1/float(n))))
