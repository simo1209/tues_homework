import functools
import turtle

import hangman
import words


def write_word(word):
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(100, 200)
    writer.write(word, font=('Arial', 16, 'bold'))
    writer.hideturtle()


# Иницилизация
original_word = words.get_random_word()
word = '_' * len(original_word)
write_word(word)
errors = 0


def on_key_press (key):
    global errors
    global word
    if errors <= hangman.MAX_ERRORS:
        if key in original_word:
            word = words.fill_char(key, word, original_word)
            write_word(word)
            if word == original_word:
                print('You win')
        else:
            errors += 1
            hangman.build_hangman(errors)
    else:
        print('You lost')


# Handle press keys 'a' to 'z'
for i in range(ord('a'), ord('z') + 1):
    key = chr(i)
    turtle.onkey(functools.partial(on_key_press, key), key)

turtle.listen()
turtle.mainloop()
