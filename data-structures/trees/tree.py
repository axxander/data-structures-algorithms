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


	# def remove(self, node):
	# 	"""Finds given node and removes it from the tree.

	# 	Args:
	# 		node (Node): Object of class Node.
	# 	"""
	# 	if not self.root:  # empty tree
	# 		return False
	# 	else:
	# 		current = self.root
	# 		parent = None
	# 		while True:
	# 			if current.value < node.value and current.right:  # traverse right
	# 				parent = current
	# 				current = current.right
	# 			elif current.value >= node.value and current.left:  # traverse left
	# 				parent = current
	# 				current = current.left
	# 			elif current.value == node.value:  # at node that needs removing
	# 				# Removed node has no right child...
	# 				if not current.right:  
	# 					if not parent:  # removed node is the root
	# 						self.root = current.left
	# 					else:  # removed node is not the root
	# 						if current.value <= parent.value:  # child of removed node sits on the left
	# 							parent.left = current.left
	# 						elif current.value > parent.value:  # child of removed node sits on the right
	# 							parent.right = current.left
	# 					return

	# 				# Right child does not have a left child
	# 				elif not current.right.left:
	# 					current.right.left = current.left
	# 					if not parent:
	# 						self.root = current.right
	# 					else:
	# 						if current.value <= parent.value:
	# 							parent.left = current.right
	# 						elif current.value > parent.value:
	# 							parent.right = current.right
	# 					return

	# 				# Right child has a left child
	# 				else:
	# 					leftmost = current.right.left
	# 					leftmostparent = current.right
	# 					while leftmost.left:
	# 						leftmostparent = leftmost
	# 						leftmost = leftmost.left

	# 					leftmostparent = leftmost.right
	# 					leftmost.left = current.left
	# 					leftmost.right = current.right

	# 					if not parent:
	# 						self.root = leftmost
	# 					else:
	# 						if current.value <= parent.value:
	# 							parent.left = leftmost
	# 						elif current.value > parent.value:
	# 							parent.right = leftmost
	# 					return


if __name__ == '__main__':

	n1 = Node(10)
	n2 = Node(20)
	n3 = Node(30)
	n4 = Node(25)
	n5 = Node(12)

	tree = BinarySearchTree(n1)

	tree.insert(n2)
	tree.insert(n3)
	tree.insert(n4)
	tree.insert(n5)

	print(n1)
	print(n2)
	print(n3)
	print(n4)
	print(n5)

	tree.remove(n2)

	print(n1)
	print(n3)
	print(n4)
	print(n5)

	# x = tree.lookup(n2)
	# print(x)





