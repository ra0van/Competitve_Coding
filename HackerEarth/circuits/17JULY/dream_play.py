#Partial
#https://www.hackerearth.com/challenge/competitive/july-circuits-17/algorithm/dramplay-and-upside-down-da5a5a5c/

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    return L[m][n]

s = raw_input()
# print s,s[::-1]
if s == s[::-1]:
    print 0
else:
    l = len(s)
    b = s[:(l/2)]
    e = s[-(l/2):]
    diff = 0
    # e1 = e[::-1]
    # for i in xrange(l/2):
    #     if b[i]!=e1[i]:
    #         diff += 1
    
    # app = ''
    # i = 0
    # new = s+app
    # while i<l and new != new[::-1]:
    #     app = s[i]+app
    #     new = s+app    
    #     i += 1
    # if i < diff:
    #     print i
    # else:
    #     print diff
    print max(len(b),len(e)) - lcs(b,e[::-1])