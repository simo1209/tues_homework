def evens_count(numbers):
	even=0
	for number in numbers:
		if number%2==0:
			even=even+1
	print(even)

evens_count([1, 2 ,4])	
