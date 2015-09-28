#http://codeforces.com/contest/581/problem/0
# AC
# time : 46ms
a,b = map(int,raw_input().split())

diff = min(a,b)
same = abs(a-b)/2
print diff,same