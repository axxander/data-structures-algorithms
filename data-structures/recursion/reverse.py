def reverse_string(string):
	"""Reverse a string using recursive method.
	   Time complexity O(n). Space complexity O(n).

	Args:
		string (str): String to reverse.
	"""
	if len(string) < 1:
		return False
	elif len(string) == 1:
		return string
	else:
		return reverse_string(string[1:]) + string[0]


def tc_reverse_string(string, a):
	"""Tail-recursive method for reversing a string.
	   Time complexity O(n^2) since prepend for all chars in string.
	   Space complexity O(1) due to tail-call optimisation. 

	Args:
		string (str): String to reverse.
		a (str): Accumulator.
	"""
	if len(string) < 0:
		return False
	elif len(string) == 1:
		return string + a
	else:
		return tc_reverse_string(string[1:], string[0] + a)



if __name__ == '__main__':

	string = 'london'

	print('String: ', string)

	x = reverse_string(string)
	print('Recursive: ', x)

	x = tc_reverse_string(string, "")
	print('Tail-call Recursive: ', x)