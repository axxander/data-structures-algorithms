def recursive_factorial(n):
	"""Recursive implementation of factorial function.

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


def iterative_factorial(n):
	"""Iterative implementation of factorial function.

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

	x = recursive_factorial(5)
	print('Recursive: ', x)

	x = iterative_factorial(5)
	print('Iterative: ', x)

