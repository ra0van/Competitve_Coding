#https://www.codechef.com/problems/TOURISTS
from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.V = vertices # no of vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

def EulerianPath(graph):
	odd = [x for x in graph.keys() if len(graph[x])&1]
	odd.append(graph.keys()[0])
	if len(odd)>3:
		return None
	stack = [odd[0]]
	path = []

	while stack:
		v = stack[-1]
		if graph[v]:
			u = graph[v][0]
			stack.append(u)
			del graph[u][graph[u].index(v)]
			del graph[v][0]
		else:
			path.append(stack.pop())
	return path

n,e = map(int,raw_input().split())
g1 = Graph(n)
uArr = []
vArr = []
for i in xrange(e):
	a,b = map(int,raw_input().split())
	uArr.append(a)
	vArr.append(b)
	g1.addEdge(a,b)
ans = EulerianPath(g1.graph)
if ans == None:
	print 'NO'
else:
	if (len(ans)==e+1 and ans[0]==ans[-1]):
		temp = defaultdict(dict)
		print 'YES'
		for i in xrange(len(ans)-1,0,-1):
			temp[ans[i]][ans[i-1]] = True
		for i in range(e):
			try:
				if temp[uArr[i]][vArr[i]]==True:
					print uArr[i],vArr[i]
				else:
					print vArr[i],uArr[i]
			except:
				print vArr[i],uArr[i]
	else:
		print "NO"
