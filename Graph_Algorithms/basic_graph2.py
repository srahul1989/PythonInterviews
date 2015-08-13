#
#
#####
graph = {
			"a" : ["d"],
			"b" : ["c"],
			"c" : ["b","c","d","e"],
			"d" : ["a","c"],
			"e" : ["c"],
			"f" : []
		}

def generate_edges(graph):
	edges = []
	for node in graph:
		for neighbour in graph[node]:
			edges.append((node, neighbour))
	return edges

def find_isolated_graph(graph):
	isolated = []
	for node in graph:
		if not graph[node]:
			isolated += node
	return isolated

def find_path(start_vertex):
	pass


print "get edges of the graph::"
print generate_edges(graph)

print "get isolated nodes : "
print find_isolated_graph(graph)