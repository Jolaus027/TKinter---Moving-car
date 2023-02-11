
import tkinter
canvas = tkinter.Canvas(width=1000,height=600)
canvas.pack()

#PANDRLAK
canvas.create_oval(50,75,20,25, width = 5, tag = "si")
canvas.create_line(35,75,35,150, width = 5,tag = "si")
canvas.create_line(35,150,45,180, width = 5,tag = "si")
canvas.create_line(35,150,25,180, width = 5,tag = "si")
canvas.create_line(35,150-75,25,150, width = 5,tag = "si")
canvas.create_line(35,150-75,45,150, width = 5,tag = "si")

#SEMAFOR
canvas.create_rectangle(15,35,55,160, fill="black")
canvas.create_line(35,75,35,250, width=10) 
canvas.create_oval(50,75,20,40,fill="red", tag="cervena")
canvas.create_oval(50,115,20,80, tag="oranzova")
canvas.create_oval(50,155,20,120, tag="zelena")

#CESTA A BUGATTI
canvas.create_line (0, 250, 1000, 250, width=5)
canvas.create_line (0, 550, 1000, 550,width=5)
canvas.create_rectangle(700, 230, 900, 370, fill= "red", tag= "bugatti")
              
number=1
semafor=1

while 1:
    if number == 1:
        #POHYB PANAKA DO PRAVA  
        if canvas.coords("si")[2] < 800:
            canvas.move("si", 5, 0)
            canvas.after(50)
            canvas.update()
        #PANAK NASTUPUJE DO AUTA
        if canvas.coords("si")[3] < 230 and canvas.coords("si")[2] >= 800: 
            canvas.move("si", 0, 5)
            canvas.after(50)
            canvas.update()
        #PANAK ZMIZNE
        if canvas.coords("si")[3] >= 230 and canvas.coords("si")[2] >= 800: 
            canvas.delete("si")
            number = 0
    else:
        if semafor == 1:
            #POHYB AUTA K SEMAFORU
            if canvas.coords("bugatti")[0] > 200:
                canvas.move("bugatti", -5, 0)
                canvas.after(50)
                canvas.update()
            #PREPINANIE FARIEB SEMAFORU
            if canvas.coords("bugatti")[0] <= 200:
                canvas.after(5000)
                canvas.update() 
                canvas.itemconfig("cervena", fill="black")
                canvas.itemconfig("oranzova", fill="orange")
                canvas.after(1000)
                canvas.update() 
                canvas.itemconfig("cervena", fill="black")
                canvas.itemconfig("oranzova", fill="black")
                canvas.after(1000)
                canvas.update() 
                canvas.itemconfig("oranzova", fill="black")
                canvas.itemconfig("zelena", fill="green")
                semafor = 0
        #POHYB AUTA DALEJ        
        else:
            canvas.move("bugatti", -5, 0)
            canvas.after(50)
            canvas.update()
                
tkinter.mainloop()
