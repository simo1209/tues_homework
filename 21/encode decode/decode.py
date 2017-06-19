cipher = {
	'h': 'i',
	'y': 'j', 
	'o': 'e',
	't': 'r', 
	'n': 'w',
	'p': 'm'
	}

cipher1 = {
	'p': 'm', 
	'r': 'o',
	'f': 'g'
	}
	
cipher2 = {
	'r': 'f',
	'o': 'h', 
	'i': 'u', 
	'm': 'z', 
	'g': 's', 
	'a': 't',
	'p': 'w',
	'n': 'y'
}

cipher3 = {
	'b': 'a'
	}
def decoding(encrypted, ciph):
	for i in encrypted:
		if i in ciph:
			encrypted.replace(i,ciph[i])
	return encrypted
print(decoding('mjriew', cipher))
print(decoding('omg' , cipher1))
print(decoding('wfhsftzzuys', cipher2))
print(decoding('bbbbbbbbbbbbbbbbbbbbbbbbbbb' , cipher3))
