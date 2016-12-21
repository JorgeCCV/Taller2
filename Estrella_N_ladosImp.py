###Estrella impar n lados
import turtle
t=turtle.Pen()

a=int(input("Ingrese las puntas de la estrella:"))
t.reset()
if a%2 ==0:
    for x in range(a):
        t.forward(200)
        t.left((a-2)*180/a)
        t.left((a-2)*180/a)
else:
    print("Ingrese un valor impar")
