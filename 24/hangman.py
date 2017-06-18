import turtle

MAX_ERRORS = 5

hangman_builder = turtle.Turtle()
hangman_builder.penup()
hangman_builder.goto(-100, 0)
hangman_builder.pendown()
hangman_builder.color("black")
#hangman_builder.ht()
w=80
def build_hangman(step):
    if step == 1:
        
        hangman_builder.fd(w)
        hangman_builder.bk(w*2)
        hangman_builder.fd(w)
        hangman_builder.right(90)
        pass
    elif step == 2:
        hangman_builder.fd(w*3/4)
        pass
    elif step == 3:
        hangman_builder.right(90)
        hangman_builder.circle(w/4)
        hangman_builder.penup()
        hangman_builder.left(90)
        hangman_builder.fd(w*2/4)
        pass
    elif step == 4:
        hangman_builder.right(90)
        hangman_builder.pendown()
        hangman_builder.circle(w)
        hangman_builder.penup()
        hangman_builder.left(90)
        hangman_builder.fd(w)
        hangman_builder.right(90)
        hangman_builder.fd(w)
        hangman_builder.pendown()
        hangman_builder.fd(w)
        hangman_builder.penup()
        hangman_builder.bk(w*3)
        hangman_builder.left(180)
        hangman_builder.pendown()
        hangman_builder.fd(w)
        hangman_builder.penup()
        hangman_builder.bk(w*2)
        hangman_builder.right(90)
        #hangman_builder.fd(w*2)
        pass
    elif step == 5:
        pass
    # Добавете до MAX_ERRORS стъпки
    else:
        print('You lost')


if __name__ == '__main__':
    for step in range(1, MAX_ERRORS + 1):
        build_hangman(step)

