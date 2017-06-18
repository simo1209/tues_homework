Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def concat_lists(first, second):
	result=[]
	for chars in first:
		result.append(chars)
	for chars in second:
		result.append(chars)
	print (result)

	
>>> concat_lists([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> 
