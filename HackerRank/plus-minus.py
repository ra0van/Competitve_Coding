t = int(raw_input())
a = map(int,raw_input().split(' '))

p=0;n=0;z=0

for i in range(t):
	if a[i]>0:
		p += 1
	elif a[i]<0:
		n += 1
	elif a[i]==0:
		z += 1

print(p/float(t))
print(n/float(t))
print(z/float(t))
