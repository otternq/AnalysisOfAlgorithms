from SetGraph import relink, dfs
#dictionary/list representaion of a graph

print("Dictionary/List Start")
digraph = {
	"a": ["b", "c", "d"],
	"b": [],
	"c": ["e", "f"]
}

print(digraph)

#all the nodes available from "a"
print(digraph["a"])

print("Dictionary/List End\n\n")

print("List/List Start")
#list/list representaion of a graph
digraph = [
	[1,2,3],
	[],
	[4,5],
	[5],
	[0],
	[8],
	[]
]

print(digraph)

print("List/List End\n\n")

#list/set
print("List/Set Start");

digraph = [
	{1, 2, 3},
	set(),
	{4, 5},
	{5},
	set(),
	{8},
	{7},
	set(),
	set()
]

print(digraph)
print(digraph[0])
print("There are " + str(len(digraph)) + " nodes")

print("Relink the digraph")
relink(digraph)

print("Digraph now looks like")
print(digraph)


def initFillArray(size, value):
	"""
	Class example was called array

	Keyword arguments:
		size - how many elements should be created
		value - the values to initalize each element to
	"""
	a = []
	for i in range(0, size):
		a.append(value)
	return a

print(initFillArray(len(digraph), False))

visit = initFillArray(len(digraph), False)
print(visit)
dfs(digraph, visit, 0)
print(visit)

print("List/Set END\n\n")