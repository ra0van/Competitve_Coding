#TLE
from sys import stdin,stdout

def isPalin(num):
	if num == num[::-1]:
		return True
	return False

def is9s(num):
	l = len(num)
	if num == '9'*l:
		return True
	return False

def getPalinFromLeft(left):
	n = int(left)
	n+= 1
	return str(n)

def getReplacingDigit(left,right):
	left = left[::-1]
	for j in range(len(right)):
		if left[j]!=right[j]:
			return j
	return -1

def main():
	t = int(stdin.readline())
	for _ in range(t):
		num = stdin.readline()
		num = num.rstrip()
		finalPalin = ''
		l = len(num)
		if isPalin(num):
			if(is9s(num)):
				ones = 2
				zeros = l-1
				finalPalin = '1'+'0'*zeros+'1'
			else:
				if l%2==1:
					mid = l/2
					left = getPalinFromLeft(num[0:mid+1])
					right = left[::-1]
					right = right[1:]
					finalPalin = left+right
				else:
					mid = (l/2 )
					left = getPalinFromLeft(num[0:mid])
					right = left[::-1]
					finalPalin = left+right
		else:
			if l%2 == 0:
				mid = l/2
				left = num[0:mid]
				right = num[mid:]
				# print left,right
				changeIndex = getReplacingDigit(left,right)
				if int(right[changeIndex]) < int(left[::-1][changeIndex]) : 
					right = left[::-1]
					finalPalin = left+right
				else:
					left = getPalinFromLeft(left)
					right = left[::-1]
					finalPalin = left+right
			else:
				mid = l/2
				left = num[0:mid+1]
				right = num[mid:]
				# print left,right
				changeIndex = getReplacingDigit(left,right)
				if(int(right[changeIndex]) < int(left[::-1][changeIndex])):
					right = left[::-1]
					right = right[1:]
					finalPalin = left+right
				else:
					left = getPalinFromLeft(left)
					right = left[::-1]
					right = right[1:]
					finalPalin = left+right
		print finalPalin
			
					



if __name__ == "__main__":
	main()
