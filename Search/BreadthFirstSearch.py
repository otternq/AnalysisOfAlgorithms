def bfs(graph, node):

	visit = array(len(graph), False)

	queue = [node]

	visit[node] = True

	while len(queue) > 0:

		node = popRight(queue)

		for n in graph[node]:

			#inspect element if it has not been inspected before
			if visit[n] == False:

				#set element to inspected
				visit[n] = True
				pushLeft(queue, n)