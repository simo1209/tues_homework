def concat_lists(first, second):
	result=[]
	for chars in first:
		result.append(chars)
	for chars in second:
		result.append(chars)
	print (result)


def number_to_list(number):
	digits=[]
	while number!=0:
		digit= number % 10
		digits.insert(0, digit)
		number = number // 10
	print(digits)


def list_to_number(digits):
	number = 0
	for char in digits:
		number = number * 10 + char
	print(number)
