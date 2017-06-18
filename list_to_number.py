Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def list_to_number(digits):
	number = 0
	for char in digits:
		number = number * 10 + char
	print(number)

	
>>> list_to_number([246])
246
>>> list_to_number([2,4,6])
246
>>> 
