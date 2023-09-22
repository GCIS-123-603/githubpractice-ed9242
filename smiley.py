import turtle as t

def smiley():
    t.begin_fill()
    t.goto(0,0)
    t.circle(100)
    t.fillcolor('yellow')
    t.end_fill()
    input('Enter to continue please...')


def small():
    t.begin_fill()
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.circle(10)
    t.fillcolor('red')
    t.end_fill()
    t.hideturtle()
    input('Enter to continue please...')



def right_eye():
    t.penup()
    t.goto(-50,125)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.fillcolor('white')
    t.end_fill()
    t.penup()
    t.goto(-50,130)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.fillcolor('blue')
    t.end_fill()
    
    input('Enter to continue please...')

def left_eye():
    t.penup()
    t.goto(50,125)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.fillcolor('white')
    t.end_fill()
    t.penup()
    t.goto(50,130)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.fillcolor('blue')
    t.end_fill()
    input('Enter to continue please..')


def smile():
    t.penup()
    t.right(90)
    t.goto(-50,60)
    t.pendown()
    t.begin_fill()
    t.circle(50,180)
    t.fillcolor('black')
    t.end_fill()
    input('Enter to continue please...')


def main():
    smiley()
    small()
    right_eye()
    left_eye()
    smile()
    

main()





