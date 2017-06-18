Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def concat_lists(first, second):
	result=[]
	for chars in first:
		result.append(chars)
	for chars in second:
		result.append(chars)
	print (result)

	
>>> def number_to_list(number):
	digits=[]
	while number!=0:
		digit= number % 10
		digits.insert(0, digit)
		number = number // 10
	print(digits)

	
>>> def list_to_number(digits):
	number = 0
	for char in digits:
		number = number * 10 + char
	print(number)
