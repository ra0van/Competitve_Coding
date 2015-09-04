def readGraph():
	graph = {}
	print "Enter No of nodes"
	n = int(raw_input())
	print "Enter Node and all edges from it. Ex: 2 : 3 4 1 0"
	for i in range(n):
		s = raw_input().split(':')
		key = map(str,s[0].split())
		value = map(str,s[1].split())
		graph[key[0]] = set(value)
	return  graph



def dfs_cycle(graph,start):
	visited = set()
	stack = [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			ext = graph[vertex]
			for node in ext:
				if (node in stack) or (node in visited):
					print "Cycle: "+vertex+"->"+node
				else:
					stack.extend(node)
					# print stack



graph = readGraph()
print "Enter Starting Node"
ch = raw_input()
dfs_cycle(graph,ch)