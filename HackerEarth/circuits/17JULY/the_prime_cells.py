#https://www.hackerearth.com/challenge/competitive/july-circuits-17/algorithm/pythagorean-triangles-0158a4c5/

n = input()
a = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
for _ in xrange(n):
    tmp = map(int,raw_input().split())
    a.append(tmp)
count = 0
for i in xrange(n):
    for j in xrange(n):
        sum = 0
        if i-1>=0:
            sum += a[i-1][j]
        if i+1<n:
            sum += a[i+1][j]
        if j-1>=0:
            sum += a[i][j-1]
        if j+1<n:
            sum += a[i][j+1]
        if sum in primes:
            count +=1 
print count