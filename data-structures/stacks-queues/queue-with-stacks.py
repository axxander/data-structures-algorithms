class Node:
	
	def __init__(self, value):
		self.value = value

class Queue:

	def __init__(self):
		self.left_stack = []
		self.right_stack = []

	def peek(self):
		"""View node at the front of the queue.
		   This is the top of the right stack.
		   O(1) time complexity.
		"""
		
		if not self.right_stack:
			while self.left_stack:
				self.right_stack.append(self.left_stack.pop())
		return self.right_stack[-1]

	def push(self, node):
		"""Add node to back of the queue (enqueue).
		   This is equivalent to pushing onto the left stack.
		   O(1) time complexity.
		"""

		self.left_stack.append(node)


	def pop(self):
		"""Remove node at the front of the queue (dequeue).
		   If the right stack is empty, we need to push all nodes to the right stack.
		   The top of the right stack is then the front of the queue.
		   If nodes already exist on the right stack, simply pop the right stack.
		   O(1) amortised time complexity -- O(n) worst case.
		"""

		self.peek()
		return self.right_stack[-1]

	def empty(self):
		"""Returns whether list is empty,
		"""
		return not self.left_stack and not self.right_stack


if __name__ == '__main__':

	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')





