from typing import Union, List

Arr = List[Union[int, float, str]]  # type alias for array

class Array:

	def __init__(self) -> None:
		self.length = 0
		self.data: Arr = []

	def push(self, item: Union[int, float, str]) -> None:
		"""Add element to end of array"""

		self.data.append(item)
		self.length += 1

	def lookup(self, index: int) -> Union[int, float, str]:
		"""Return item at specified index"""

		try:
			return self.data[index]
		except IndexError as e:
			raise e

	def pop(self) -> Union[int, float, str, None]:
		"""Remove and return the last item in the array"""

		if self.length:
			self.length -= 1
			return self.data.pop()
		else:
			return None

	def insert(self, item: Union[int, float, str], index: int) -> None:
		"""Insert item at specified index in the array"""

		try:
			self.data.append(item)
			self.data[index], self.data[index+1:] = self.data[-1], self.data[index:-1]
			self.length += 1
		except IndexError as e:
			raise e

	def delete(self, index: int) -> None:
		"""Delete item at specified index"""

		try:
			self.data[index:-1], self.data[-1] = self.data[index+1:], self.data[index]
			_tmp = self.pop()
		except IndexError as e:
			raise e


	def __str__(self) -> str:
		"""Formatted string for printing object instance"""

		return f'Length: {self.length}    Data: {self.data}'
