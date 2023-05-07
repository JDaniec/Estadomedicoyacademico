from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk


#Ventana principal
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("Estado Medico y Estudiantil")

# tamaño de la ventana
ventana_principal.geometry("500x650")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

#Fondo para la ventana principal
imagen_fondo = Image.open("img/Fondo.jpg")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
fondo = Label(ventana_principal, image=imagen_fondo)
fondo.place(x=0, y=0, height=700, width=500)

#-----variables------
ventana_principal.resizable(0,0)
name = StringVar()
edad = StringVar()
codigo = StringVar()
programa = ["Ingeniería de Sistemas", "Ingeniería Industrial", "Ingeniería Civil", "Ingeniería Mecánica", "Ingeniería Química", "Ingeniería Electrica", "Ingeniería Electrónica", "Turismo"]
programa_selectec = StringVar()


#--------------------------------
# frame titulo
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="peach puff", width=480, height=50, borderwidth=5 , relief="groove")
frame_entrada.place(x=10, y=10)

titulo = Label(frame_entrada, text="Informe Estudiantil")
titulo.config(bg = "peach puff",fg="black", font=("Ubuntu Light", 19))
titulo.place(x=130,y=5)

#-----------------------------------------------
#Frame entrada de datos
#------------------------------------
frame_2 = Frame(ventana_principal)
frame_2.config(bg="bisque", width=480, height=150 , borderwidth=7 , relief="groove")
frame_2.place(x=10, y=80)

# caja de texto para nombre del estudiante
entry_c = Entry(frame_2, textvariable=name)
entry_c.config(bg="white", fg="black", font=("Times New Roman", 18), width=27,)
entry_c.place(x=110,y=5)

# etiqueta para el nombre del estudiante 
lb_c = Label(ventana_principal, text = "Nombre: ")
lb_c.config(bg= "bisque", fg="blue", font=("Times New Roman", 18))
lb_c.place(x=15, y=90)

# caja de texto para la edad del estudiante
entry_c = Entry(frame_2, textvariable=edad)
entry_c.config(bg="white", fg="black", font=("Times New Roman", 18), width=6,)
entry_c.place(x=320,y=45)

# etiqueta para la edad del estudiane
lb_c = Label(ventana_principal, text = "Edad: ")
lb_c.config(bg ="bisque", fg="blue", font=("Times New Roman", 18))
lb_c.place(x=260, y=130)

# caja de texto para codigo del estudiante
entry_c = Entry(frame_2, textvariable=codigo)
entry_c.config(bg="white", fg="black", font=("Times New Roman", 18), width=8,)
entry_c.place(x=100,y=45)

# etiqueta para el codigo del estudiante 
lb_c = Label(ventana_principal, text = "Codigo: ")
lb_c.config(bg = "Bisque", fg="blue", font=("Times New Roman", 18))
lb_c.place(x=18, y=130)

# etiqueta para el programa del estudiante 
lb_c = Label(ventana_principal,textvariable=programa, text = "Programa : ")
lb_c.config(bg="bisque",fg="blue", font=("Times New Roman", 18))
lb_c.place(x=14, y=170)

#Seleccion de porograma academico
cmb_programa = ttk.Combobox(ventana_principal, textvariable=programa_selectec, values=programa, font=("Times New Roman", 17))
cmb_programa.place(x=130, y=180)


#--------------------------------
# frame 3
#--------------------------------
frame_3 = Frame(ventana_principal)
frame_3.config(bg="peach puff",width=480, height=50, borderwidth=5 , relief="groove")
frame_3.place(x=10, y=250)

titulo2 = Label(frame_3, text="Estado Medico y Estudiantil")
titulo2.config(bg="peach puff",fg="black", font=("MS Sans Serif", 19))
titulo2.place(x=80,y=4)
#--------------------------------
# frame 3
#--------------------------------
frame_3 = Frame(ventana_principal)
frame_3.config(bg="bisque",width=230, height=240, borderwidth=5 , relief="groove")
frame_3.place(x=10, y=320)
#--------------------------------
# frame 4
#--------------------------------
frame_3 = Frame(ventana_principal)
frame_3.config(bg="bisque",width=230, height=240, borderwidth=5 , relief="groove")
frame_3.place(x=260, y=320)












#---------------------------------------------------
ventana_principal.mainloop()