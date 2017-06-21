def main():
	n = input()
	a = map(int,raw_input().split())
	a.sort()
	rev = 0
	x,y = n,1

	for i in a:
		rev += (x-y)i
		x -= 1
		y += 1
	print rev

if __name__ == '__main__':
	main()