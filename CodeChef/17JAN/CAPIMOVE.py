#TLE

from sys import stdin,stdout
for t in xrange(input()):
	result = ''
	n= int(raw_input().strip())
	population = map(int,raw_input().strip().split())
	pop_city_map = []
	#print population,pop_city_map
	for i in xrange(n):
		pop_city_map.append([population[i]])
	
	for i in xrange(n-1):
		a,b = map(int,raw_input().split())
		pop_city_map[a-1].append(population[b-1])
		pop_city_map[b-1].append(population[a-1])
	
	for i in xrange(n):
		d = set(pop_city_map[i])
		rem = list(set(population)-d)
		if len(rem)==0:
			result = result + ' ' + str(0)
		else:
			# print d,rem
			result = result + ' ' + str(population.index(max(rem))+1)
	print result.strip()

		
