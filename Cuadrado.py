####Definir una función para un cuadrado de lado n:
import turtle
t=turtle.Pen()

a=int(input("Ingrese la longitud del cuadrado:"))
size=a
def micuadrado(size):
    for x in range(1,5):
        t.forward(size)
        t.left(90)

micuadrado(a)
