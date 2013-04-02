from SetGraph import relink, depthFirstSearch, isconnected, initFillArray, numberit
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


print(initFillArray(len(digraph), False))

visit = initFillArray(len(digraph), False)
print(visit)
depthFirstSearch(digraph, visit, 0)
print(visit)

print(isconnected(digraph))
print(numberit(digraph))

print("List/Set END\n\n")