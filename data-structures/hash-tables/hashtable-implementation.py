class Hashtable:
	
	def __init__(self):
		"""Define size of hashmap, i.e. allowed addresses.
		"""

		self.length = 50
		self.hashtable = [None for _ in range(self.length)]

	def __str__(self):
		return str(self.__dict__)

	def _hash(self, key):
		"""Hash function using Unicode integer of each character in string key.
		   Quasi-O(1) operation since we assume the length of the key is << total 
		   number of key-value pairs.
		"""

		hash = 0
		for i in range(len(key)):
			hash = (hash + ord(key[i])) % self.length
		return hash


	def set(self, key, value):
		"""Insert buckets (key-value pairs) in memory address allocated by hashing
		   function. O(1) operation.
		"""

		address = self._hash(key)
		if self.hashtable[address]:  # not empty
			self.hashtable[address].append([key, value])
		else:  # empty
			self.hashtable[address] = []
			self.hashtable[address].append([key, value])


	def get(self, key):
		"""Iterate through non-empty addresses and return value if
		   keys match. O(1) operation assumed. Maximum number of collisions is O(n),
		   where n is the number of key-value pairs.
		"""

		address = self._hash(key)
		try:
			for bucket in self.hashtable[address]:
				if bucket[0] == key:
					return bucket[1]
			return 'Key not valid...'
		except: 
			return 'Key not valid...'


	def keys(self):
		"""List all keys in hashtable.
		   O(n+m) operation where n is the size of the hashtable and m the number of collisions.
		"""

		keys_array = []
		for address in range(self.length):
			if self.hashtable[address]:  # not empty
				for bucket in self.hashtable[address]:
					keys_array.append(bucket[0])
		return keys_array



if __name__ == '__main__':

	h = Hashtable()

	h.set('grapes', 100)
	h.set('apples', 50)
	h.set('oranges', 5)

	x = h.get('apples')
	print(x)

	print(h)

	x = h.keys()
	print(x)

	


