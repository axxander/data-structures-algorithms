def recursive_factorial(n):
	"""Recursive implementation of factorial function.
	   Time complexity O(n). Space complexity O(n).

	Args:
		n (int): Factorial input.

	"""
	if n < 0:
		return False
	elif n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n * recursive_factorial(n-1)


def tc_recursive_factorial(n, a):
	"""Tail-call optimisation version of recurssive fatorial.
	   Uses recursion without a call-stack. Stack-overflow is no longer
	   an issue.
	   Compilers convert this to iterative -- best of both worlds,
	   recursive code but implemented in iterative manner.
	   Time complexity O(n). Space complexity O(1).

	Args:
		n (int): Factorial input.
		a (int): Accumulator.
	"""

	if n < 0:
		return False
	elif n < 2:
		return a
	else:
		return tc_recursive_factorial(n-1, n*a)


def iterative_factorial(n):
	"""Iterative implementation of factorial function.
	   Time complexity O(n). Space complexity O(1).

	Args:
		n (int): Factorial input.

	"""
	if n < 0:
		return False
	elif n < 2:
		return 1
	else:
		value = 1
		for i in range(2, n+1):
			value *= i
		return value


if __name__ == '__main__':

	n = 5

	x = recursive_factorial(n)
	print('Recursive: ', x)

	x = iterative_factorial(n)
	print('Iterative: ', x)

	x = tc_recursive_factorial(n, 1)
	print('Tail-call Recursive: ', x)




