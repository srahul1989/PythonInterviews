#
#
#######

class Graph(object):

	def __init__(self, graph_dict={}):
		self.__graph_dict = graph_dict

	def vertices(self):
		return list(self.__graph_dict.keys())

	def edges(self):
		return self.__generate_edges()

	def add_vertex(self, vertex):
		if vertex not in self.__graph_dict:
			self.__graph_dict[vertex] = []

	def add_edge(self, edge):
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.__graph_dict:
			self.__graph_dict[vertex1].append(vertex2)
		else:
			self.__graph_dict[vertex1] = [vertex2]

	def __generate_edges(self):
		edges = []
		for vertex in self.__graph_dict:
			for neighbour in self.__graph_dict[vertex]:
				if {neighbour, vertex} not in edges:
					edges.append({vertex, neighbour})
		return edges

	def __str__(self):
		res = "vertices:"
		for k in self.__graph_dict:
			res += str(k) + " "
		res += "\nedges: "
		for edge in self.__generate_edges():
			res += str(edge) + " "
		return res

	def find_path(self, start_vertex, end_vertex, path=[]):
		graph = self.__graph_dict
		path = path + [start_vertex]
		if start_vertex == end_vertex:
			return  path
		if start_vertex not in path:
			return None
		print "graph of start[vertex] : ", graph[start_vertex]
		for vertex in graph[start_vertex]:
			extended_path = ""
			if vertex not in path:
				extended_path = self.find_path(vertex, end_vertex, path)
			if extended_path:
				return extended_path
		return None

	def vertex_degree(self, vertex):
		print "self.__graph_dict: ", self.__graph_dict
		adj_vertices = self.__graph_dict[vertex]
		print "adjucent virtices: ", adj_vertices
		degree = len(adj_vertices) + adj_vertices(vertex)
		return degree


if __name__ == "__main__":
	g = {
			"a" : ["d"],
			"b" : ["c"],
			"c" : ["b","c","d","e"],
			"d" : ["a","c"],
			"e" : ["c"],
			"f" : []
		}
	graph = Graph(g)
	print "virtices of the graph: ", graph.vertices()
	print "edges of graphs: ", graph.edges()
	graph.add_vertex("z")	
	print "virtices of the graph: ", graph.vertices()
	graph.add_edge({"a", "z"})
	print "edges of graphs: ", graph.edges()
	print "virtices of the graph: ", graph.vertices()
	print "find path: ", graph.find_path("a", "d")
	print "vertex Degree:: ", graph.vertex_degree("a")
