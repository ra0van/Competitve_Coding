
def bfs(graph,start):
	visited,queue = set(),[start]
	while queue:
		vertex = queue.pop()
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)

	return visited

def dfs_paths(graph,start,goal):
	queue = [(start,[start])]

	while queue:
		(vertex,path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path+[next]
			else:
				queue.append((next,path+[next]))

def shortestPath(graph,start,goal):
	try:
		return next(dfs_paths(graph,start,goal))
	except StopIteration:
		return None

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print bfs(graph,'A')
print list(dfs_paths(graph,'A','F'))
print shortestPath(graph,'A','F')