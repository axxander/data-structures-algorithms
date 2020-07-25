import random

def bubble_sort(arr):
	"""Sorts a given array into ascending order using the bubble sort
	   algorithm.

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


if __name__ == '__main__':

	# generate random array
	arr = [random.randint(0, 100) for _ in range(10)]

	# built-in sort
	sort = sorted(arr)
	print('Built-in sort: {}'.format(sort))

	# test bubble sort
	sort = bubble_sort(arr)
	print('Bubble sort: {}'.format(sort))

	# test selection sort
	sort = selection_sort(arr)
	print('Selection sort: {}'.format(sort))



