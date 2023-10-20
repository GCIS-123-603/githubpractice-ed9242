import turtle as t 

t.Screen() # creating a screen for the turtle animation

t.tracer(0) # implementing a tracer function to skip the turtle animation

def squares(colors): # creating a function which will draw a square/ pixel with a color as a parameter
    t.fillcolor(colors)
    t.begin_fill()
    for i in range(4):
        t.fd(20)
        t.rt(90)
    t.fd(20)
    t.end_fill()
    input('Enter to continue please...')



def black_pixel(): # function for black pixel
    colors="black"
    squares(colors)

def white_pixel(): # function for white pixel
    colors="white"
    squares(colors)

def red_pixel():   # function for red pixel
    colors="red"
    squares(colors)
    
def yellow_pixel():  # function for yellow pixel
    colors="yellow"
    squares(colors)

def orange_pixel():  # function for orange pixel
    colors="orange"
    squares(colors)

def green_pixel():  # function for green pixel
    colors="green"
    squares(colors)

def yellowgreen_pixel():  # function for yellow green pixel
    colors="yellowgreen"
    squares(colors)

def sienna_pixel():  # function for sienna pixel
    colors="sienna"
    squares(colors)

def tan_pixel(): # function for tan pixel
    colors="tan"
    squares(colors)

def gray_pixel(): # function for gray pixel
    colors="gray"
    squares(colors)

def darkgray_pixel(): # function for darkgray pixel
    colors="darkgray"
    squares(colors)


