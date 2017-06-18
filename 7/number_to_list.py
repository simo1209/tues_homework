Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def number_to_list(number):
	digits=[]
	while number!=0:
		digit= number % 10
		digits.insert(0, digit)
		number = number // 10
	print(digits)

	
>>> number_to_list(987)
[9, 8, 7]
>>> 
