import turtle

tablero=turtle.Screen()
tablero.title("Holaaaa")
tablero.bgcolor("black")
tablero.setup(width=800,height=600)

cuadrado2=turtle.Turtle()
cuadrado=turtle.Turtle()
cuadrado.shape("square")
cuadrado.color("red")
cuadrado2.shape("square")
cuadrado2.color("green")
count=0
while True:
    count+=1
    tablero.update()
    cuadrado.forward(1)
    cuadrado.left(1)
   
    cuadrado2.right(1)
    cuadrado2.forward(1)
    if count==90:
        cuadrado.color("yellow")
    elif count ==180:
        cuadrado.color("green")
        
    elif count == 270: 
        cuadrado.color("white")
    elif count == 359:
        cuadrado.color("brown")
    
    
   



