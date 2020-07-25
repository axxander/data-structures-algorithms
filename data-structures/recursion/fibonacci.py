def recursive_fib(n):
	"""Recursive implementation of fibonacci sequence.
	   Time complexity O(2^n) -- exponential!

	Args:
		n (int): Fibonacci number.

	"""
	if n <= 0:
		return False
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return recursive_fib(n-1) + recursive_fib(n-2)


def iterative_fib(n):
	"""Iterative implementation of fibonacci numbers.
	   Time complexity O(n).

	Args:
		n (int): Fibonacci number.

	"""
	if n <= 0:
		return False
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		fnums = [0, 1]
		for i in range(2, n):
			fnums.append(fnums[i-1] + fnums[i-2])
		return fnums[-1]


if __name__ == '__main__':

	x = recursive_fib(10)
	print('Recursive: ', x)

	x = iterative_fib(10)
	print('Iterative: ', x)


