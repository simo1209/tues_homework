Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def split_change(change):
	X = change//5
	Y = (change-X*5)//2
	Z = change-X*5-Y*2
	if X==0:
		print(Y,'* 2')
		print(Z,'* 1')
	elif Y==0:
		print(X,'* 5')
		print(Z,'* 1')
	elif Z==0:
		print(X,'* 5')
		print(Y,'* 2')
	else:
		print(X,'* 5')
		print(Y,'* 2')
		print(Z,'* 1')

		
>>> 
