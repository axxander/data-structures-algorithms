class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(Node):

	def __init__(self, head):
		self.head = head
		self.tail = self.head
		self.length = 1  # Keep track of number of nodes in linked list

	def append(self, node):
		"""Appends node to end of linked list
		"""

		current = self.head
		if self.head:  # linked list is not empty
			while current.next:  # next element not null
				current = current.next
			current.next = node  # append new node
			self.tail = node
		else:  # empty linked list
			self.head = node

		self.length += 1


	def prepend(self, node):
		"""Appends node to the front of linked list.
		"""

		current = self.head
		self.head = node
		self.head.next = current
		self.length += 1


	def insert(self, node, position):
		"""Inserts a node in linked list at a given postion.
		"""

		current = self.head
		current_position = 1
		if position < 1 or position > self.length:  # invalid
			return 'Invalid index. Must be more than zero and less than the length of the list...'
		elif position > 1:  # insert
			while current_position < position and current:
				if current_position == position - 1:
					node.next = current.next
					current.next = node
				current = current.next
				current_position += 1
		else:  # prepend
			node.next = self.head
			self.head = node

		self.length += 1


	def remove(self, position):
		"""Removes node in linked list at a given position.
		"""

		current = self.head
		current_position = 1
		if position < 1 or position > self.length:  # invalid position
			return 'Invalid index. Must be more than zero and less than the length of the list...'
		elif position > 1:  # beyond head node
			while current_position < position and current:
				if current_position == position - 1:  # node before one being removed
					current.next = current.next.next
				current = current.next
				current_position += 1
		else:  # delete head node
			self.head = current.next

		self.length -= 1


	def lookup(self, position):
		"""Returns the node value at the given position.
		"""

		current = self.head
		current_position = 1
		if position < 1 or position > self.length:  # invalid position
			return 'Invalid index. Must be more than zero and less than the length of the list...'
		elif position > 1:  # beyond head node
			while current_position < position and current:
				if current_position == position - 1:  # node before one being read
					return 'Value at position {} is {}.'.format(position, current.next.value)
				current = current.next
				current_position += 1
		else:  # head node
			return 'Value at position {} is {}.'.format(position, self.head.value)


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


if __name__ == '__main__':

	node1 = Node(10)
	node2 = Node(20)
	node3 = Node(30)
	node4 = Node(40)
	node5 = Node(0)
	node6 = Node(-10)
	node7 = Node('insert')

	ll = LinkedList(node1)
	ll.append(node2)
	ll.append(node3)
	ll.append(node4)
	ll.prepend(node5)
	ll.prepend(node6)
	ll.insert(node7, 3)

	print(ll)

	ll.remove(3)
	ll.remove(1)
	ll.remove(1)

	print(ll)

	x = ll.lookup(2)
	print(x)
