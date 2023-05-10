from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk


#top level formulario
def abrir_toplevel_medico():
    global toplevel_medico
    toplevel_medico = Toplevel()
    toplevel_medico.title("Formulario Medico")
    toplevel_medico.resizable(False, False)
    toplevel_medico.geometry("400x400")
    toplevel_medico.config(bg="white")

    # etiqueta para "Formulario Medico"
    lb_c = Label(toplevel_medico, text = "Fomulario medico ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=10, y=10)

    # Combobox para el género
    cmb_genero = ttk.Combobox(toplevel_medico, textvariable=generos_selected, values=generos, font=("Helvetica", 12))
    cmb_genero.place(x=110, y=50)

    #label para nombrar cada combo o lo que sea
    #nombre
    lb_g = Label(toplevel_medico, text = "Genero: ")
    lb_g.config(bg= "white", fg="blue", font=("Times New Roman", 15))
    lb_g.place(x=15, y=50)

    # Combobox para el tipo de sangre
    cmb_sangre = ttk.Combobox(toplevel_medico, textvariable=sangre_seleccionado, values=tipos_desangre, font=("Helvetica", 12))
    cmb_sangre.place(x=160, y=80)   

    #label para nombrar cada combo o lo que sea
    #nombre
    lb_s = Label(toplevel_medico, text = "Tipo de Sangre: ")
    lb_s.config(bg= "white", fg="blue", font=("Times New Roman", 15))
    lb_s.place(x=15, y=80)

   # boton para aceptar
    bt_aceptar = Button(toplevel_medico,text="Listo", command=aceptar)
    bt_aceptar.place(x=290, y=350, width=100, height=30)

# aceptar
def aceptar():
    global generos_selected
    global genero_seleccionado
    global sangre_seleccionado
    genero_seleccionado = generos_selected.get()
    toplevel_medico.destroy()
    

#top level formulario acedemico
def abrir_toplevel_academico():
    global toplevel_academico
    toplevel_academico = Toplevel()
    toplevel_academico.title("Formulario Acamedico")
    toplevel_academico.resizable(False, False)
    toplevel_academico.geometry("400x400")
    toplevel_academico.config(bg="white")

    # etiqueta para "Formulario Academico"
    lb_c = Label(toplevel_academico, text = "Fomulario Academico ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=10, y=10)
    
   # boton para aceptar
    bt_aceptar1 = Button(toplevel_academico, text="Listo", command=aceptar1)
    bt_aceptar1.place(x=290, y=350, width=100, height=30)

# aceptar
def aceptar1():
    toplevel_academico.destroy()
    
#top level para mostrar resultados
def abrir_toplevel_resultados(): 
    global toplevel_resultados       
    toplevel_resultados = Toplevel()
    toplevel_resultados.title("Resultados")
    toplevel_resultados.resizable(False, False)
    toplevel_resultados.geometry("400x600")
    toplevel_resultados.config(bg="white")
    #nombre
    lb_nombre = Label(toplevel_resultados, text="Nombre: {}".format(name.get()))
    lb_nombre.place(x=10, y=20)

    #nombre
    lb_programa = Label(toplevel_resultados, text="Programa académico: {}".format(programa_selectec.get()))
    lb_programa.place(x=10, y=40)

    #codigo
    lb_codigo = Label(toplevel_resultados, text="Codigo: {}".format(codigo.get()))
    lb_codigo.place(x=10, y=60)

    #edad
    lb_codigo = Label(toplevel_resultados, text="Edad: {}".format(edad.get()))
    lb_codigo.place(x=10, y=80)

    # Crear una etiqueta para mostrar el género
    lb_genero = Label(toplevel_resultados, text="Género: {}".format(genero_seleccionado))
    lb_genero.config(bg="white", font=("Helvetica", 12))
    lb_genero.place(x=10, y=100)

    #tipo de sangre
    lb_sangre = Label(toplevel_resultados, text="Tipo de sangre: {}".format(sangre_seleccionado.get()))
    lb_sangre.config(bg="white", font=("Helvetica", 12))
    lb_sangre.place(x=10, y=120)


# borrar
def borrar():
    messagebox.showinfo("Estado", "Los datos serán borrados")
    name.set("")
    generos_selected.set("") # borra el valor seleccionado en el combobox de género
    sangre_seleccionado.set("")
# salir
def salir():
    messagebox.showinfo("Estado", "La app se va a cerrar")
    ventana_principal.destroy()


#Ventana principal
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("Estado Medico y Estudiantil")

# tamaño de la ventana
ventana_principal.geometry("500x550")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

#Fondo para la ventana principal
imagen_fondo = Image.open("img/Fondo.jpg")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
fondo = Label(ventana_principal, image=imagen_fondo)
fondo.place(x=0, y=0, height=700, width=500)

#-----variables------
name = StringVar() 
edad = StringVar()
codigo = StringVar()
programa = ["Ingeniería de Sistemas", "Ingeniería Industrial", "Ingeniería Civil", "Ingeniería Mecánica", "Ingeniería Química", "Ingeniería Electrica", "Ingeniería Electrónica", "Turismo"]
programa_selectec = StringVar()
generos = ["Femenino", "Masculino"]
generos_selected = StringVar()
genero_seleccionado = StringVar()
tipos_desangre = ["Tipo B+", "Tipo B+", "Tipo A+", "Tipo O+", "Tipo B-", "Tipo B-", "Tipo A-", "Tipo O-"]
sangre_seleccionado = StringVar()

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
entry_c = Entry(frame_2, textvariable=name)

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
cmb_programa = ttk.Combobox(ventana_principal, textvariable=programa_selectec, values=programa, font=("Times New Roman", 15))
cmb_programa.place(x=125, y=180)


#--------------------------------
# frame 3
#--------------------------------
frame_3 = Frame(ventana_principal)
frame_3.config(bg="peach puff",width=480, height=50, borderwidth=5 , relief="groove")
frame_3.place(x=10, y=250)

titulo2 = Label(frame_3, text="Estado Medico y Academico")
titulo2.config(bg="peach puff",fg="black", font=("MS Sans Serif", 19))
titulo2.place(x=80,y=4)
#--------------------------------
# frame 4
#--------------------------------
frame_4 = Frame(ventana_principal)
frame_4.config(bg="bisque",width=230, height=110, borderwidth=5 , relief="groove")
frame_4.place(x=10, y=320)
#--------------------------------
# frame 5
#--------------------------------
frame_5 = Frame(ventana_principal)
frame_5.config(bg="bisque",width=230, height=110, borderwidth=5 , relief="groove")
frame_5.place(x=260, y=320)

# boton para abrir Toplevel para ingresar formulario medico
bt_fm = Button(frame_4, text="Formulario Medico", command=abrir_toplevel_medico)
bt_fm.config(height=3, width=25)
bt_fm.place(x=15, y=20)

# boton para abrir Toplevel para ingresar formulario academico
bt_fm = Button(frame_5, text="Formulario Academico", command=abrir_toplevel_academico)
bt_fm.config(height=3, width=25)
bt_fm.place(x=15, y=20)

# boton para abrir resultados
bt_r = Button(ventana_principal, text="Mostrar informe", command=abrir_toplevel_resultados)
bt_r.config(height=3, width=20)
bt_r.place(x=320, y=470)

# boton para borrar
bt_r = Button(ventana_principal, text="Borrar", command=borrar)
bt_r.config(height=3, width=20)
bt_r.place(x=150, y=470)






#---------------------------------------------------
ventana_principal.mainloop()