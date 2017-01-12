from sys import stdin,stdout
for t in xrange(input()):
	result = ''
	n= int(stdin.readline().strip())
	population = map(int,stdin.readline().strip().split())
	sort_pop = sorted(population)
	pop_city_map = {}
	pop_matrix = []
	#print population,pop_city_map
	for city,pop in enumerate(population):
		pop_city_map[str(pop)] = city+1
		pop_matrix.append([pop])
	# for i in xrange(n):
	# 	pop_city_map.append([population[i]])
	
	for i in xrange(n-1):
		a,b = map(int,stdin.readline().split())
		pop_matrix[a-1].append(population[b-1])
		pop_matrix[b-1].append(population[a-1])
	
	for i in xrange(n):
		d = set(pop_matrix[i])

		for i in xrange(n):
			val = sort_pop[n-1-i]

			if val not in d:
				result = result + ' ' + str(pop_city_map[str(val)])
				break;
		else:
			result = result + ' 0'
	stdout.write(result.strip()+'\n') 
