Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def split_change(change):
	a=0
	b=0
	c=0
	while change>=2:
		a = a + 1
		change = change - 2
	while change>=5:
		b = b + 1
		change = change - 5
	if a!=0:
		print a,        '*2'
	if b!=0:
		print b,        '*5'
	if change != 0:
		print change,        '*1'

		
>>> split_change(87)
43 *2
1 *1
>>> 
