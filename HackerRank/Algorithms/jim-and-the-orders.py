# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/jim-and-the-orders
#AC
n = input()
a = []
s = []
for i in range(n):
    cus = map(int,raw_input().split())
    a.append(cus)
    tmp = [cus[0]+cus[1],i]
    s.append(tmp)
s = sorted(s)
for i in range(n):
    print s[i][1]+1,