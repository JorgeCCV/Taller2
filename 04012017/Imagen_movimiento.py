from tkinter import *
import time
tk=Tk()

####Carga una imagen
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

my_image=PhotoImage(file="nave.gif")
canvas.create_image(0,0,anchor=NW,image=my_image)

###Animacion
for x in range(-10,50):
    canvas.move(1,5,0)
    tk.update()
    time.sleep(0.05)
    
for x in range(0,60):
        canvas.move(1,0,5)
        tk.update()
        time.sleep(0.05)
    
for x in range(0,60):
            canvas.move(1,-5,0)
            tk.update()
            time.sleep(0.05)
    
for x in range(0,60):
                canvas.move(1,0,-5)
                tk.update()
                time.sleep(0.05)
    
tk.mainloop()

