import sys
import os

# Required to run script from parent directory (or any other)
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..'))

import unittest
from arrays import Array


class TestSortMethods(unittest.TestCase):

	def setUp(self):
		self.array = Array()
		self.array.data = [1, 2, 3, 4, 5]
		self.array.length = 5

	def test_push(self):

		# standard tests
		self.array.push(6)
		self.assertEqual(self.array.data, [1, 2, 3, 4, 5, 6])
		self.assertEqual(self.array.length, 6)

	def test_lookup(self):

		# standard tests
		self.assertEqual(self.array.lookup(0), 1)
		self.assertEqual(self.array.lookup(3), 4)

		# exceptions tests
		with self.assertRaises(IndexError):
			self.array.lookup(20)

	def test_pop(self):

		# standard tests
		self.assertEqual(self.array.pop(), 5)
		self.assertEqual(self.array.length, 4)
		self.assertEqual(self.array.pop(), 4)
		for _ in range(3):
			self.array.pop()
		self.assertEqual(self.array.pop(), None)  # empty array
		self.assertEqual(self.array.length, 0)

	def test_insert(self):

		# standard tests
		self.array.insert(10, 0)  # first element
		self.assertEqual(self.array.data, [10, 1, 2, 3, 4, 5])
		self.array.insert(20, 5)  # last element
		self.assertEqual(self.array.data, [10, 1, 2, 3, 4, 20, 5])
		self.array.insert(30, 2)  # middle element
		self.assertEqual(self.array.data, [10, 1, 30, 2, 3, 4, 20, 5])
		self.assertEqual(self.array.length, 8)

		# exceptions tests
		with self.assertRaises(IndexError):
			self.array.insert(40, 20)  # out of bounds

	def test_delete(self):

		# standard tests
		self.array.delete(0)
		self.assertEqual(self.array.data, [2, 3, 4, 5])  # first element
		self.array.delete(3)
		self.assertEqual(self.array.data, [2, 3, 4])  # last element
		self.array.delete(1)
		self.assertEqual(self.array.data, [2, 4])  # middle element
		self.assertEqual(self.array.length, 2)

		# exception errors
		with self.assertRaises(IndexError): 
			self.array.delete(20)  # out of bounds


if __name__ == '__main__':
	unittest.main()