def recursive_fib(n):
	"""Recursive implementation of fibonacci sequence.
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
		prev = 1
		prevprev = 0
		for i in range(3, n+1):
			current = prev + prevprev  # fib number equals sum of previous two
			prevprev = prev
			prev = current
		return current


if __name__ == '__main__':

	x = recursive_fib(10)
	print('Recursive: ', x)

	x = iterative_fib(10)
	print('Iterative: ', x)


