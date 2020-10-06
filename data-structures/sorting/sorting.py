import random

def bubble_sort(arr):
	"""Sorts a given array into ascending order using the bubble sort
	   algorithm.
	   Time complexity O(n^2). Space complexity O(1).

	Args:
		arr (list, dtype=float/int): Array to sort in ascending order. 

	"""
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr


def selection_sort(arr):
	"""Sorts a given array into ascending order using selection
	   sort algorithm.
	   Time complexity O(n^2). Space complexity O(1).

	Args:
		arr (list, dtype=float/int): Array to sort in ascending order.

	"""
	for i in range(len(arr)):
		min_index = i  # initialise index of number to compare
		for j in range(i+1, len(arr)):

			if arr[j] < arr[min_index]:  # update index minimum number of subarray
				min_index = j

		arr[i], arr[min_index] = arr[min_index], arr[i]  # swap minimum of subarray with index adjacent to global minimum

	return arr


def insertion_sort(arr):
	"""Sorts a given array into ascending order using insertion
	   sort algorithm.
	   Time complexity: Best case O(n) and worst case O(n^2). Space complexity O(1).
	   Good for nearly sorted/sorted arrays.

	Args:
		arr (list, dtype=float/int): Array to sort in ascending order.

	"""
	for i in range(len(arr)):
		if arr[i] <= arr[0]:  # smallest element so far
			arr = [arr[i]] + arr[:i] + arr[i+1:]
		else:
			for j in range(1, i):  # iterate through left subarray
				if arr[i] > arr[j-1] and arr[i] <= arr[j]:  # > than previous and <= than next
					arr = arr[:j] + [arr[i]] + arr[j:i] + arr[i+1:]
	return arr


def merge_sort(arr):
	"""Sorts a given array into ascending order using merge
	   sort algorithm.
	   Time complexity is O(nlogn). Space complexity is O(n).

	   Time complexity of this speicific part is O(logn).

	Args:
		arr (list, dtype=float/int): Array to sort in ascending order.

	"""	
	if len(arr) == 1:  # base case
		return arr
	else:
		center = int(len(arr)/2)  # center index of subarray
		left = arr[:center]
		right = arr[center:]
		return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
	"""Merges two arrays into single array, in ascending order.
	   This specific step is O(n) time complexity.

	Args:
		left (list, dtype=float/int): Subarray.
		right (list, dtype=float/int): Subarray.

	"""
	print(left, right)
	arr = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr.append(left[i])
			i += 1
		else:
			arr.append(right[j])
			j += 1

	arr = arr + left[i:] + right[j:]  # concatenate rest of subarray

	return arr


def quick_sort(arr):
	
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr.pop()

	left = []
	right = []

	for num in arr:
		if num > pivot:
			right.append(num)
		else:
			left.append(num)

	return quick_sort(left) + [pivot] + quick_sort(right)

	



if __name__ == '__main__':

	# built-in sort
	arr = [random.randint(0, 100) for _ in range(10)]
	sort = sorted(arr)
	print('Built-in sort: {}'.format(sort))

	# test bubble sort
	arr = [random.randint(0, 100) for _ in range(10)]
	sort = bubble_sort(arr)
	print('Bubble sort: {}'.format(sort))

	# test selection sort
	arr = [random.randint(0, 100) for _ in range(10)]
	sort = selection_sort(arr)
	print('Selection sort: {}'.format(sort))

	arr = [random.randint(0, 100) for _ in range(10)]
	sort = insertion_sort(arr)
	print('Insertion sort: {}'.format(sort))

	# Merge sort
	arr = [random.randint(0, 100) for _ in range(10)]
	sort = merge_sort(arr)
	print('Merge sort: {}'.format(sort))

	# Quick sort
	arr = [random.randint(0, 100) for _ in range(10)]
	sort = quick_sort(arr)
	print('Quick sort: {}'.format(sort))





