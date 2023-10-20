import turtle as t #importing turtle module and assigining it a variable 

color = {'0':'black','1':'red'}  # initializing a dictionary where the key is the no which the user has to type and the value is the color

t.tracer(0) # implementing a tracer function to skip the turtle animation

def squares(): # function to create 1 singluar pixel 
    for i in range(4):
        t.fd(20)
        t.rt(90)
    t.fd(20)

def row1(x, y):  # function that creates 1 row containing 20 squares/pixels of alternating color 
    for i in range(20):
        if i % 2 == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            squares()
            t.fillcolor(color['0'])
            t.end_fill()
        else:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            squares()
            t.fillcolor(color['1'])
            t.end_fill()
        x += 20

def row2(x, y): # function that creates another row of 20 squares/pixels of alternating color different to that of row1(x,y)
    for i in range(20):
        if i % 2 == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            squares()
            t.fillcolor(color['1'])
            t.end_fill()
        else:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            squares()
            t.fillcolor(color['0'])
            t.end_fill()
        x += 20

x = -200   # initializing the starting coordinates of the checkerboard (they are global variables)
y = -200

for i in range(10):
    row1(x, y)                # running a for loop that repeats fucntions row1(x,y) and row2(x,y) 
    y += 20                   # one after the other and also adding 20 to the global variable y 
    row2(x, y)
    y += 20
input('Enter to exit please..')


