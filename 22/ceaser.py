def encrypt(text, key):
	Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	chipher=[]
	for symbol in text:
		i=Alphabet.index(symbol)
		chipher.append(Alphabet[i+key])
	print(chipher)

encrypt('HELLO', 1)


