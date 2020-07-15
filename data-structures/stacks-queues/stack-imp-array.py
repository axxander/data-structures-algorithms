class Node:
	
	def __init__(self, value):
		self.value = value

class Stack(Node):

	def __init__(self):
		self.array = []

	def peek(self):
		"""View value of top of the stack.
		   O(1) time complexity.
		"""
		return self.array[-1].value

	def push(self, node):
		"""Add node to the top of the stack.
		   O(1) time complexity.
		"""

		if isinstance(node, Node):
			self.array.append(node)
		else:
			return print('Error. Node provided is not an instance of class Node...')


	def pop(self):
		"""Remove node at the top of the stack.
		   O(1) time complexity.
		"""

		if self.array:
			self.array.pop()
		else:
			return 'Error. Stack already empty...'


	def __str__(self):
		"""Formatted print for stack.
		"""

		string = ''
		for node in reversed(self.array):
			string += ' {} \n---\n'.format(node.value)
		string += 'nul'

		return string


if __name__ == '__main__':

	print('Initialise stack...')
	stack = Stack()

	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')

	print('Pushing nodes...')
	stack.push(a)
	stack.push(b)
	stack.push(c)
	stack.push(d)

	print('Current stack...\n')
	print(stack)

	print('\nPop stack once...')
	stack.pop()

	print('New stack is...\n')
	print(stack)

	print('\nPeek stack value is...')
	x = stack.peek()
	print(x)

	# print('\nPrint node b...')
	# print(b)

	# print('\nPrint node a...')
	# print(a)




