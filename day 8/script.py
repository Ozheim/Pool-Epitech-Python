from turtle import * 

#task 2.1
 
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)


# task 2.2
import turtle
toto = turtle.Screen ()
toto.bgcolor ("black")
titi = turtle.Turtle ()
titi.color ("blue")
for i in range (3) :
    titi.right (90)
titi.circle (42)
toto.exitonclick ()

#task 2.3: 

def draw_polygon(sides): 
    
    if sides == 3: 
        toto = turtle.Screen ()
        forward(50)
        left(120)
        forward(50)
        left(120)
        forward(50)
        toto.exitonclick ()
    if sides == 4: 
        for i in range(0,4):
            forward(50)
            left(90)
            i+=1
    if sides == 5: 
            for i in range(0,5):
                 forward(100)
                 left(72)
                 i+=1
      
    if sides == 6:
        for i in range (0,6):
            forward(100)
            left(60)
            i+=1


draw_polygon(6)


#task 2.4 

def spirale():
    color("red")
    width("50")
    for i in range(0,360): 
        forward(i)
        left(20)
        
spirale()

