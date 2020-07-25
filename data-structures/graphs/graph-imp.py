class Node:
	"""Element of graph.

	Attributes:
		value (int): Value of element.
	"""
	def __init__(self, value):
		self.value = value

class Graph:
	"""Unweighted and undirected graph implementation using adjacent list.
	   Assuming node values are unique.

	Attributes:
		number_of_nodes (int): Total number of vertexes in the graph.
		adjacent_list (dict): Represents conenctions between nodes. Key is a node and value is
							  an array of connected nodes.
	"""

	def __init__(self):
		self.number_of_nodes = 0
		self.adjacent_list = {}


	def add_vertex(self, node):
		"""Adds a vertex to the graph.

		Args:
			node (Node): Node/vertex being added to the graph.
		"""	
		if node not in self.adjacent_list:  # add key to adjacent list if not currently in it
			self.adjacent_list[node] = []
			self.number_of_nodes += 1
		else:  # node already in the graph
			return False


	def add_edge(self, node1, node2):
		"""Adds a bidirectional connection between the two given nodes.

		Args:
			node1 (Node): Vertex within the graph.
			node2 (Node): Vertex within the graph.
		"""
		if node1 in self.adjacent_list and node2 in self.adjacent_list:  # nodes are in the graph
			self.adjacent_list[node1].append(node2)
			self.adjacent_list[node2].append(node1)
		else:  # at least one node is not in the graph
			return False

	def __str__(self):
		"""Formatted output for viewing graph. Outputs the nodes and all nodes they are conected to.

		Args:
			None.
		"""
		string = ''
		for key in self.adjacent_list:
			string += '{} --> {}\n'.format(key.value, ''.join(str(connection.value) + ' ' for connection in self.adjacent_list[key]))
		return string


if __name__ == '__main__':

	# Construct Node objects to add to graph
	n0 = Node(0)
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n6 = Node(6)

	# Constrcut graph
	g = Graph()

	# Add nodes to the graph
	g.add_vertex(n0)
	g.add_vertex(n1)
	g.add_vertex(n2)
	g.add_vertex(n3)
	g.add_vertex(n4)
	g.add_vertex(n5)
	g.add_vertex(n6)

	# Add connections between nodes
	g.add_edge(n0, n1)
	g.add_edge(n0, n2)
	g.add_edge(n1, n2)
	g.add_edge(n1, n3)
	g.add_edge(n3, n4)
	g.add_edge(n2, n4)
	g.add_edge(n4, n5)
	g.add_edge(n5, n6)

	# Print graph (shows connections)
	print(g)






