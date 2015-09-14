#http://codeforces.com/contest/577/problem/B
def check(sum,m):
	if sum!=0 and sum%m==0:
		return True
	return False

Flag = False
n,m = map(int,raw_input().split())
a = map(int,raw_input().split())

for i in range(n):
	if Flag:
		break;
	sum = a[i]
	if check(sum,m):
		Flag = True
		break;

	for j in range(n):
		if i!=j:
			sum += a[j]
		if check(sum,m):
			Flag = True
			break;
if Flag:
	print "YES"
else:
	print "NO"