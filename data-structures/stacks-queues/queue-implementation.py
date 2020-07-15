class Node:
	
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		if self.next:
			string = 'Node value: {}. Next value: {}.'.format(self.value, self.next.value)
		else:
			string = 'Node value: {}. Next value: {}.'.format(self.value, 'null')

		return string


class Queue:

	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0


	def peek(self):
		"""View value at the front of the queue
		   O(1) time complexity.
		"""
		
		if self.first:
			return self.first.value
		else:
			return print('Error. Queue is currently empty...')


	def enqueue(self, node):
		"""Add node to back of the queue.
		   O(1) time complexity.
		"""

		if isinstance(node, Node):  # input is instance of class Node
			if self.length:  # non-empty queue
				self.last.next = node
				self.last = node
			else:  # empty queue
				self.first = node
				self.last = node
		else:  # input not instance of class Node
			return print('Error. Input node is not an instance of class Node...')

		self.length += 1


	def dequeue(self):
		"""Removes node from front of queue.
		   O(1) time complexity.
		"""

		if self.first:  # non-empty queue
			if self.length > 1:  # more than one node
				self.first = self.first.next
			else:  # remove last node
				self.first = None
				self.last = None			
		else:  # empty queue
			return print('Error. Queue is already empty...')

		self.length -= 1


	def __str__(self):
		"""Formatted print for queue.
		"""

		if self.length:
			string = ''
			current = self.first
			while current.next:
				string += '{} -- '.format(current.value)
				current = current.next
			string += str(current.value) + ' -- null'
		else:
			string = 'null'

		return string

if __name__ == '__main__':

	print('Initialise queue...')
	q = Queue()

	a = Node('xander')
	b = Node('george')
	c = Node('megan')
	d = Node('ellie')

	print('Enqueuing nodes...')
	q.enqueue(a)
	q.enqueue(b)
	q.enqueue(c)
	q.enqueue(d)

	print('Current queue...\n')
	print(q)

	print('\nDequeuing queue once...')
	q.dequeue()

	print('New queue is...\n')
	print(q)

	print('\nPeek queue value is...')
	x = q.peek()
	print(x)

	print('\nPrint node b...')
	print(b)

	print('\nPrint node c...')
	print(c)




