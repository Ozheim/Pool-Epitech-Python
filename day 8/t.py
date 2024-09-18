import turtle 
from turtle import * 


def flower():
   

    while True:
        titi = turtle.Turtle ()
        
        titi.circle(100)
        titi.forward(90)
        if abs(pos()) < 1:
            break

flower()

    


