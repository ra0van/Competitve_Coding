# https://www.hackerrank.com/contests/hour-of-code-2016/challenges/playlist-length
n = input()
time = 0
for i in xrange(n):
    m,s = map(int,raw_input().split())
    time += m*60 + s
h = time/3600
time = time%3600
m = time/60
time = time%60
print h,m,time
