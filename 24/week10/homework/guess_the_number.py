from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 10

number = str(randint(MIN_NUMBER, MAX_NUMBER))
name = input("Enter your name: ")
print("Hello", name, "!")
play = True
while play:
    i = 0
    while i < 3:
        guess = input("Number:")
        if guess == number:
            print("You won!")
            wannaPlay = input("Play again: ")
            if wannaPlay == 'yes':
                i = 0
                continue
            elif wannaPlay == 'no':
                break
                # else:
        i += 1
    print("you lost")
    wannaPlay = input("Play again: ")
    if wannaPlay == 'yes':
        continue
    else:
        break
