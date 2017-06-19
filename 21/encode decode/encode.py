cipher = {
	'i': 'h',
	'j': 'y', 
	'e': 'o',
	'r': 't', 
	'w': 'n',
	'm': 'p'
	}

cipher1 = {
	'm': 'p', 
	'r': 'o',
	'g': 'f'
	}
	
cipher2 = {
	'f': 'r',
	'h': 'o', 
	'u': 'i', 
	'z': 'm', 
	's': 'g', 
	't': 'a',
	'w': 'p',
	'y': 'n'
}

cipher3 = {
	'a': 'b'
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
