def first_recurring_char(arr):
	"""Use a hashmap for constant lookup to check if we have
	   already seen a given value. O(n) time complexity since
	   only one iteration of array required (in worst case).
	   Space complexity O(n).
	"""

	hashtable = {}
	for char in arr:
		if char in hashtable:  # found recurring character
			return char
		else:  # first occurence of character
			hashtable[char] = 1

	return None  # no recurring character

def naive_first_recurring_char(arr):
	"""Use two pointers. Record left-most recurring character.
	   O(n^2) time complexity. Space complexity O(1).
	"""
	right = len(arr)
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] == arr[j]:
				if j < right:
					right = j
					val = arr[i]

	try:
		return val
	except:
		return None  # no recurring character


if __name__ == '__main__':
	
	arr = [2, 5, 5, 2, 3, 5, 1, 2, 4]
	ans = 5

	if naive_first_recurring_char(arr) == ans:
		print(True)
	else:
		print(False)

	if first_recurring_char(arr) == ans:
		print(True)
	else:
		print(False)

