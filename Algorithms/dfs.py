# depth first search on graphs with an adjacency matrix
# requires python for the module dfs_paths_itr
def dfs_itr(graph,start):
	visited = set()
	stack = ['A']

	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

def dfs_rec(graph,start,visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	for next in graph[start]-visited:
		dfs_rec(graph,next,visited)

	return visited

def dfs_paths(graph,start,goal,path=None):
	if path is None:
		path = [start]

	if start == goal:
		yield path

	for next in graph[start]-set(path):
		yield  dfs_paths(graph,next,goal,path+[next])

def dfs_paths_itr(graph,start,goal,path=None):
	stack = [(start,[start])]
	while stack:
		(vertex,path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path+[next]
			else:
				stack.append((next,path+[next]))


graph = {'A' : set(['B','C']),
		'B' : set(['A','D','E']),
		'C' : set(['A','F']),
		'D' : set(['B']),
		'E' : set(['B','F']),
		'F' : set(['C','E'])}

# print dfs_itr(graph,'A')
# print dfs_rec(graph,'A')
print list(dfs_paths(graph,'A','F'))