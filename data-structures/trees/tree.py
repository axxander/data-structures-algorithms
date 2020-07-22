class Node:
	"""Elements of a tree.

	Attributes:
		value (int): Value of node.
		left (Node): Points to left child node of current node.
		right (Node): Points to right child node of current node.
	"""
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		"""Print function for node object. Prints left node value/null,
		   current node value and then the right node value/null.
		"""
		if not self.left and not self.right:
			left = False
			right = False
		elif not self.left:
			left = False
			right = True
		elif not self.right:
			left = True
			right = False
		else:
			left = True
			right = True

		return '{} -- {} -- {}'.format(self.left.value if left else 'null',
									   self.value,
									   self.right.value if right else 'null')



class BinarySearchTree:
	"""Implementation of binary tree data structure.

	Attributes:
		root (Node): The root node of the tree.

	"""
	def __init__(self, root):
		self.root = root


	def insert(self, node):
		"""Inserts a given node into the tree.

		Args:
			node (Node): Object of class Node.
		"""
		if not self.root:  # empty tree
			self.root = node
		else:  # non-empty tree
			current = self.root
			while True:
				if current.value < node.value:  # traverse right
					if current.right:  # not a leaf
						current = current.right
					else:  # is a leaf
						current.right = node
						return
				elif current.value >= node.value:  # traverse left
					if current.left:  # not a leaf
						current = current.left
					else:  # is a leaf
						current.left = node
						return		


	def lookup(self, node):
		"""Lookup to see if node exists in tree. 

		Args:
			node (Node): Object of class Node.
		"""
		if not self.root:  # empty tree
			return False
		else:  # non-empty tree
			current = self.root
			while True:
				if current.value == node.value:  # value found
					return current
				elif current.value < node.value:  # traverse right
					if current.right:
						current = current.right
					else:
						return False
				elif current.value >= node.value:  # traverse left
					if current.left:
						current = current.left
					else:
						return False


if __name__ == '__main__':

	n1 = Node(10)
	n2 = Node(20)
	n3 = Node(30)
	n4 = Node(5)
	n5 = Node(8)
	n6 = Node(1)
	null = Node(0)

	tree = BinarySearchTree(n1)

	tree.insert(n2)
	tree.insert(n3)
	tree.insert(n4)
	tree.insert(n5)
	tree.insert(n6)

	print(n1)
	print(n2)
	print(n4)

	x = tree.lookup(n2)
	print(x)





