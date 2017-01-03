###Estrella impar n lados
import turtle
t=turtle.Pen()

a=int(input("Ingrese las puntas de la estrella:"))
t.reset()
if a%2 ==1:
    for x in range(a):
        t.forward(150)
        t.left((a-2)*180/a)
        t.left((a-2)*180/a)
else:
    for x in range(a):
        t.forward(150)
        t.right((a-2)*180/a)
        t.right((a-2)*270/a)
  
