def relink(g):
	#iterate through the graph indexes
	for i in range(0, len(g)):
		#iterate through current nodes children
		for j in g[i]:
			#add a link from the child to the parent
			if i != j:
				g[j].add(i)

def dfs(g, visit, node):
	visit[node] = True
	for n in g[node]:
		if visit[n] == False:
			dfs(g, visit, n)