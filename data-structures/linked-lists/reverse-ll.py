class Node:

	def __init__(self, value):
		self.value = value
		self.next = None
		self.previous = None


class LinkedList(Node):

	def __init__(self, head):
		self.head = head
		self.tail = self.head
		self.length = 1  # Keep track of number of nodes in linked list

	def append(self, node):
		"""Appends node to end of linked list.
		   O(1) time complexity.
		"""

		current = self.tail
		current.next = node
		self.tail = node
		self.length += 1


	def prepend(self, node):
		"""Appends node to the front of linked list.
		   O(1) time complexity.
		"""

		current = self.head
		self.head = node
		self.head.next = current
		self.length += 1


	def insert(self, node, position):
		"""Inserts a node in linked list at a given postion.
		   O(n) time complexity.
		"""

		current = self.head
		current_position = 1
		if position < 1 or position > self.length:  # invalid position
			return 'Invalid index. Must be more than zero and less than the length of the list...'
		elif position == 1 and current:
			self.prepend(node)
		elif position == self.length and current:
			self.append(node)
		else:  # insert
			while current_position < position and current:
				if current_position == position - 1:
					node.next = current.next
					current.next = node
				current = current.next
				current_position += 1

		self.length += 1


	def remove(self, position):
		"""Removes node in linked list at a given position.
		   O(n) time complexity.
		"""

		current = self.head
		current_position = 1
		if position < 1 or position > self.length:  # invalid position
			return 'Invalid index. Must be more than zero and less than the length of the list...'
		elif position == 1 and current:  # list head
			self.head = current.next
		elif position == self.length and current:  # list tail
			while current_position < position-1 and current:
				current = current.next
				current_position += 1
			current.next = None
			self.tail = current
		else:  # between (exclusive) head and tail
			while current_position < position and current:
				if current_position == position - 1:  # node before one being removed
					current.next = current.next.next
				current = current.next
				current_position += 1

		self.length -= 1


	def lookup(self, position):
		"""Returns the node value at the given position.
		   O(n) time complexity.
		"""

		current = self.head
		current_position = 1
		if position < 1 or position > self.length:  # invalid position
			return 'Invalid index. Must be more than zero and less than the length of the list...'
		elif position == 1 and current:  # list head
			return 'Value at position {} is {}.'.format(position, self.head.value)
		elif position == self.length and current:  # list tail
			return 'Value at position {} is {}.'.format(position, self.tail.value)
		else:  # between (exclusive) head and tail
			while current_position < position and current:
				if current_position == position - 1:  # node before one being read
					return 'Value at position {} is {}.'.format(position, current.next.value)
				current = current.next
				current_position += 1


	def __str__(self):
		"""Display linked list pictorally when printed.
		"""

		string = ''  # output string
		current = self.head
		if self.head:  # list not empty
			while current.next:  # next node not null
				string += str(current.value) + ' --> '
				current = current.next
			string += str(current.value) + ' --> '
			string += 'null'
		else:  # list empty
			string = 'null'

		string += '\nHead Value: {}    Tail Value: {}    Total Nodes:{}'.format(self.head.value, self.tail.value, self.length)

		return string


	def reverse(self):
		"""Iterative method for reversing a singly linked list.
		   O(n) time complexity and O(1) space.
		"""

		if not self.head.next:  # single element contained
			return self.head
		else:
			current = self.head  # start at head
			previous = None  # previous points to null
			self.tail = current  # start becomes tail
			while current.next:
				next = current.next  # save next node
				current.next = previous  # swap pointer to previous node
				previous = current  # shift previous node to current node
				current = next  # shift current node to next node
			current.next = previous
			self.head = current  # tail becomes head

if __name__ == '__main__':

	node1 = Node(10)
	node2 = Node(20)
	node3 = Node(30)
	node4 = Node(40)
	node5 = Node(50)

	ll = LinkedList(node1)
	ll.append(node2)
	ll.append(node3)
	ll.append(node4)
	ll.append(node5)

	print(ll)

	ll.reverse()

	print(ll)


