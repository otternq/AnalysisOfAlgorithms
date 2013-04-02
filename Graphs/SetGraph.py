from copy import deepcopy

def relink(g):
	#iterate through the graph indexes
	for i in range(0, len(g)):
		#iterate through current nodes children
		for j in g[i]:
			#add a link from the child to the parent
			if i != j:
				g[j].add(i)

def depthFirstSearch(graph, visit, node):
	visit[node] = True
	for n in graph[node]:
		if visit[n] == False:
			depthFirstSearch(graph, visit, n)

def numberit(graph):
	visit = initFillArray(len(graph), 0)
	count = 0

	for n in range(0, len(graph)):
		if visit[n] == 0:
			count = numberitAux(graph, visit, n, count)

	return visit

def numberitAux(graph, visit, node, count):
	count += 1
	visit[node] = count
	for n in graph[node]:
		if visit[n] == 0:
			count = numberitAux(graph, visit, n, count)
	return count

def isconnected(graph):
	visit = initFillArray(len(graph), False)
	isconnectedAux(graph, visit, 0)
	return all(visit)

def isconnectedAux(graph, visit, node):
	print(node)

	visit[node] = True

	for n in graph[node]:
		if visit[n] == False:
			isconnectedAux(graph, visit, n)

def initFillArray(size, value):
	"""
	Class example was called array

	Keyword arguments:
		size - how many elements should be created
		value - the values to initalize each element to
	"""
	a = []
	for i in range(0, size):
		a.append(deepcopy(value))

	return a