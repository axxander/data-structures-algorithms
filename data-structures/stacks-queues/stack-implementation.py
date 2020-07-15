class Node:
	
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		"""Formatted print for node.
		"""

		if self.next:
			outstring = 'Node value: {}. Next Node value: {}'.format(self.value, self.next.value)
		else:
			outstring = 'Node value: {}. Next Node value: {}'.format(self.value, 'null')

		return outstring

class Stack:

	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0


	def peek(self):
		"""View value of top of the stack.
		   O(1) time complexity.
		"""
		return self.top.value

	def push(self, node):
		"""Add node to the top of the stack.
		   O(1) time complexity.
		"""

		if isinstance(node, Node):
			if self.top:
				current = self.top
				self.top = node
				self.top.next = current
			else:
				self.top = node

			self.length += 1
		else:
			return print('Error. Node provided is not an instance of class Node...')


	def pop(self):
		"""Remove node at the top of the stack.
		   O(1) time complexity.
		"""

		if self.top:
			self.top = self.top.next
			self.length -= 1
		else:
			return 'Error. Stack already empty...'


	def __str__(self):
		"""Formatted print for stack.
		"""

		string = ''
		current = self.top
		if current:
			while current.next:
				string += ' {} \n---\n'.format(current.value)
				current = current.next
			string += ' {} \n---\n'.format(current.value)
			string += 'nul'
		else:
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

	stack.push('q')

	print('Current stack...\n')
	print(stack)

	print('\nPop stack once...')
	stack.pop()

	print('New stack is...\n')
	print(stack)

	print('\nPeek stack value is...')
	x = stack.peek()
	print(x)

	print('\nPrint node b...')
	print(b)

	print('\nPrint node a...')
	print(a)




