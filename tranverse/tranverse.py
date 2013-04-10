treefullbinD = [{1,2}, {3,4}, {5, 6}, set(), set(), set(), set()]
nodes = ["*","+","-","X","Y","A","B"] #(X+Y)*(A-B)

def preorder(g, node, visitf):
	visitf(g, node)
	for i in g[node]:
		preorder(g, i, visitf)

def postorder(g, node, visitf):
	for i in g[node]:
		postorder(g, i, visitf)
	visitf(g, node)

def vfunc(g, node):
	print(nodes[node], end="")

preorder(treefullbinD, 0, vfunc)