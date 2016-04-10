def GetEnergy(n):
	energy = map(int,raw_input().split())
	finalEnergy = 0
	requiredEnergy = 0
	for e in energy:
		finalEnergy += e
		if(finalEnergy < 0):
			requiredEnergy += abs(finalEnergy)
			finalEnergy = 0 
	
	return requiredEnergy+1



def main():
	cases = input()
	for i in range(cases):
		size = input()
		print 'Scenario #'+str(i+1)+': '+str(GetEnergy(size))

if __name__ == '__main__':
	main()