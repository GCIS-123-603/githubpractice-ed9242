import turtle as t

t.Screen() # creating a screen for the turtle animation.

t.speed(0) # declaring the speed of the turtle ( the maximum speed is 0).

t.tracer(0) # declaring the function to skip the turtle animation.

colors = {'0':'black','1':'white','2':'red','3':'yellow','4':'orange','5':'green','6':'yellowgreen','7':'sienna','8':'tan','9':'gray','A':'darkgray'}

# creating a dictionary where each number corresponds to a particular color. 

def colored_pixel(col):  # declaring a fuction which creates a square/pixel of the desired colors whose numbers are presented in the text files.
    t.begin_fill()
    t.fillcolor(colors[col])  
    for i in range(4):
        t.fd(20)
        t.rt(90)
    t.fd(20)
    t.end_fill()

def squares(): # function to create 1 singluar pixel/square. 
    for i in range(4):
        t.fd(20)
        t.rt(90)
    t.fd(20)


def rainbow(colors):
    tokens = list(sentence)
    for token in tokens:
        if token in colors:
            t.begin_fill()
            squares()
            t.fillcolor(colors[token])
            t.end_fill()
        else:
            print('Invalid color entered:', token)
            return False
    input('Enter to exit please...')



def reading_files(): # declaring a function which wil read all the text files.
    while True:
        for i in files: 
            t.penup()
            t.goto(-200,200)
            t.pendown()
            for j in i:
                j = j.replace('\n','')
                for k in j:
                    colored_pixel(k)
                t.penup()
                t.goto(t.xcor()-(len(j)*20),t.ycor()-20)
                t.pendown()

            input("enter to continue...")
            t.clear()


f1 = open("C:/Users/LENOVO/OneDrive - GEMS EDUCATION/Documents/activity 2/drawing01.txt","r") # Opening all the text files in order to read the data present in it 
f2 = open("C:/Users/LENOVO/OneDrive - GEMS EDUCATION\Documents/activity 2/drawing02.txt","r")
f3 = open("C:/Users/LENOVO/OneDrive - GEMS EDUCATION/Documents/activity 2/drawing03.txt","r")
f4 = open("C:/Users/LENOVO/OneDrive - GEMS EDUCATION/Documents/activity 2/drawing04 (1).txt","r")

files = [f1.readlines(),f2.readlines(),f3.readlines(),f4.readlines()] # creating a list containing all the data present in each indivial text file.

sentence = input('Enter a sentence/string here: ') # creating a variable which will store a string which contains characters corresponding to particlar colors.

rainbow(colors) # calling the rainbow function which creates a row of different colored pixels

def main(): # main function which calls all the other functions present in the program and closes all the text files.
    reading_files()
    f1.close() 
    f2.close()
    f3.close()
    f4.close()


main() # calling the main funciton


