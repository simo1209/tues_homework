Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def encode_word(word, cipher):
	i=[]
	for letters in word:
		i.append(letters)
	for chars in i:
		print(cipher[chars])

		
>>> encode_word("python", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'})
m
j
r
i
e
w
>>> 
