from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk

#verificar si es un numero
def validate_number_input(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False    

def calcular_promedio():
    global promedio
    notas = []
    for entry in (Fundamentos_de_Programación, Calculo_1, Algebra_lineal, Quimica, Deportes, Taller_de_lenguage, Catedra):
        nota = entry.get()
        if nota:
            nota = float(nota)
            if nota < 0 or nota > 50:
                messagebox.showerror("Error", "El valor de la nota debe estar entre 0 y 50.")
                return
            notas.append(nota)
        else:
            messagebox.showerror("Error", "No se ha ingresado un valor para una nota.")
            return
    if notas:
        promedio = sum(notas) / len(notas)
        messagebox.showinfo("Promedio", f"El promedio es {promedio:.2f}")
    else:
        messagebox.showerror("Error", "No se han ingresado valores para las notas.")

#top level formulario
def abrir_toplevel_medico():
    global toplevel_medico
    toplevel_medico = Toplevel()
    toplevel_medico.title("Formulario Medico")
    toplevel_medico.resizable(False, False)
    toplevel_medico.geometry("400x320")
    toplevel_medico.config(bg="bisque")

    # etiqueta para "Formulario Medico"
    lb_c = Label(toplevel_medico, text = "Fomulario medico ")
    lb_c.config(bg="bisque", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=10)

    # Combobox para el género
    cmb_genero = ttk.Combobox(toplevel_medico, textvariable=generos_selected, values=generos, font=("Helvetica", 12))
    cmb_genero.place(x=110, y=50)

    #label para nombrar cada combo o lo que sea
    #nombre
    lb_g = Label(toplevel_medico, text = "Genero: ")
    lb_g.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_g.place(x=15, y=50)

    # Combobox para el tipo de sangre
    cmb_sangre = ttk.Combobox(toplevel_medico, textvariable=sangre_seleccionado, values=tipos_desangre, font=("Helvetica", 12))
    cmb_sangre.place(x=160, y=80)   

    #label para nombrar cada combo o lo que sea
    #nombre
    lb_s = Label(toplevel_medico, text = "Tipo de Sangre: ")
    lb_s.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_s.place(x=15, y=80)

    #label para nombrar cada combo o lo que sea
    #nombre
    lb_a = Label(toplevel_medico, text = "Altura (cm): ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=120)

    # caja de texto para la altura
    entry_a = Entry(toplevel_medico, textvariable=altura, validate="key", validatecommand=vcmd)
    entry_a.config(bg="white", fg="black", font=("Times New Roman", 18), width=10,)
    entry_a.place(x=120,y=120)
    
    # caja de texto para la masa
    entry_m = Entry(toplevel_medico, textvariable=masa, validate="key", validatecommand=vcmd)
    entry_m.config(bg="white", fg="black", font=("Times New Roman", 18), width=10,)
    entry_m.place(x=120,y=160)
    

    #etiquieta para masa
    lb_a = Label(toplevel_medico, text = "Masa(g): ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=160)

    #etiquieta para la enfermedad
    lb_a = Label(toplevel_medico, text = "Selecciona enfermedad(opcional)): ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=192)

    # Combobox para la enfermedad
    cmb_enfermedad = ttk.Combobox(toplevel_medico, textvariable=enfermedad_selecionada, values=enfermedades, font=("Helvetica", 12))
    cmb_enfermedad.place(x=20, y=215)  

   # boton para aceptar
    bt_aceptar = Button(toplevel_medico,text="Listo", command=aceptar)
    bt_aceptar.place(x=290, y=250, width=100, height=30)

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
    toplevel_academico.config(bg="bisque")

    frame_a1 = Frame(toplevel_academico)
    frame_a1.config(bg="peach puff", width=380, height=40, borderwidth=5 , relief="groove")
    frame_a1.place(x=10, y=50)
    lb_c = Label(frame_a1, text = "Digite las notas ")
    lb_c.config(bg="peach puff", fg="black", font=("Helvetica", 15))
    lb_c.place(x=120, y=1)

    # etiqueta para "Formulario Academico"
    lb_c = Label(toplevel_academico, text = "Fomulario Academico ")
    lb_c.config(bg="bisque", fg="black", font=("Helvetica", 18))
    lb_c.place(x=100, y=10)
    
    # caja de texto para  materia 1
    entry_ma1 = Entry(toplevel_academico,textvariable=Fundamentos_de_Programación,validate="key", validatecommand=vcmd)
    entry_ma1.config(bg="white", fg="black", font=("Times New Roman", 15), width=5)
    entry_ma1.place(x=150,y=100)

    #etiquieta para la nota de programacion
    lb_a = Label(toplevel_academico, text = "Programación: ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=100)

    # caja de texto para  materia 2
    entry_ma2 = Entry(toplevel_academico,textvariable=Calculo_1,validate="key", validatecommand=vcmd)
    entry_ma2.config(bg="white", fg="black", font=("Times New Roman", 15), width=5)
    entry_ma2.place(x=150,y=130)

    #etiquieta para la nota de calculo
    lb_a = Label(toplevel_academico, text = "Calculo 1: ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=130)

    # caja de texto para  materia 3
    entry_ma3 = Entry(toplevel_academico,textvariable=Algebra_lineal, validate="key", validatecommand=vcmd)
    entry_ma3.config(bg="white", fg="black", font=("Times New Roman", 15), width=5)
    entry_ma3.place(x=150,y=160)

    #etiquieta para la nota de programacion
    lb_a = Label(toplevel_academico, text = "Algebra: ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=160)

    # caja de texto para  materia 4
    entry_ma4 = Entry(toplevel_academico,textvariable=Taller_de_lenguage, validate="key", validatecommand=vcmd)
    entry_ma4.config(bg="white", fg="black", font=("Times New Roman", 15), width=5)
    entry_ma4.place(x=150,y=190)

    #etiquieta para la nota de programacion
    lb_a = Label(toplevel_academico, text = "Taller: ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=190)

    # caja de texto para  materia 5
    entry_ma5 = Entry(toplevel_academico,textvariable=Quimica, validate="key", validatecommand=vcmd)
    entry_ma5.config(bg="white", fg="black", font=("Times New Roman", 15), width=5)
    entry_ma5.place(x=150,y=220)

    #etiquieta para la nota de programacion
    lb_a = Label(toplevel_academico, text = "Química: ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=220)

    
    # caja de texto para  materia 6
    entry_ma6 = Entry(toplevel_academico,textvariable=Deportes, validate="key", validatecommand=vcmd)
    entry_ma6.config(bg="white", fg="black", font=("Times New Roman", 15), width=5)
    entry_ma6.place(x=150,y=250)

    #etiquieta para la nota de programacion
    lb_a = Label(toplevel_academico, text = "Deportes: ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=250)

    # caja de texto para  materia 7
    entry_ma7 = Entry(toplevel_academico,textvariable=Catedra, validate="key", validatecommand=vcmd)
    entry_ma7.config(bg="white", fg="black", font=("Times New Roman", 15), width=5)
    entry_ma7.place(x=150,y=280)

    #etiquieta para la nota de programacion
    lb_a = Label(toplevel_academico, text = "Catedra: ")
    lb_a.config(bg= "bisque", fg="black", font=("Times New Roman", 15))
    lb_a.place(x=15, y=280)

# boton para aceptar
    bt_aceptar1 = Button(toplevel_academico, text="Listo", command=calcular_promedio)
    bt_aceptar1.place(x=290, y=350, width=100, height=27)

   

#aceptar
def aceptar1():
    toplevel_academico.destroy()
  

    
    
#top level para mostrar resultados
def abrir_toplevel_resultados(): 
    global toplevel_resultados       
    toplevel_resultados = Toplevel()
    toplevel_resultados.title("Resultados")
    toplevel_resultados.resizable(False, False)
    toplevel_resultados.geometry("400x400")
    toplevel_resultados.config(bg="bisque")
    #nombre
    lb_nombre = Label(toplevel_resultados, text="Nombre: {}".format(name.get()))
    lb_nombre.config(bg="bisque", font=("Times New Roman", 12))
    lb_nombre.place(x=10, y=20)

    #programa
    lb_programa = Label(toplevel_resultados, text="Programa académico: {}".format(programa_selectec.get()))
    lb_programa.config(bg="bisque", font=("Times New Roman", 12))
    lb_programa.place(x=10, y=40)

    #codigo
    lb_codigo = Label(toplevel_resultados, text="Codigo: {}".format(codigo.get()))
    lb_codigo.config(bg="bisque", font=("Times New Roman", 12))
    lb_codigo.place(x=10, y=60)

    #edad
    lb_edad = Label(toplevel_resultados, text="Edad: {}".format(edad.get()))
    lb_edad.config(bg="white", font=("Times New Roman", 12))
    lb_codigo.place(x=10, y=80)

    # Crear una etiqueta para mostrar el género
    lb_genero = Label(toplevel_resultados, text="Género: {}".format(genero_seleccionado))
    lb_genero.config(bg="bisque", font=("Times New Roman", 12))
    lb_genero.place(x=10, y=100)

    #tipo de sangre
    lb_sangre = Label(toplevel_resultados, text="Tipo de sangre: {}".format(sangre_seleccionado.get()))
    lb_sangre.config(bg="bisque", font=("Times New Roman", 12))
    lb_sangre.place(x=10, y=120)

    #altura
    lb_altura = Label(toplevel_resultados, text="Altura (cm): {}".format(altura.get() + " cm"))
    lb_altura.config(bg="bisque", font=("Times New Roman", 12))
    lb_altura.place(x=10, y=140)

    #masa
    lb_masa = Label(toplevel_resultados, text="Masa (g): {}".format(masa.get() + " g"))
    lb_masa.config(bg="bisque", font=("Times New Roman", 12))
    lb_masa.place(x=10, y=160)

    #enfermedad
    
    lb_enfermedad = Label(toplevel_resultados, text="Enfermedad: {}".format(enfermedad_selecionada.get()))
    lb_enfermedad.config(bg="bisque", font=("Times New Roman", 12))
    lb_enfermedad.place(x=10, y=185)
    

    lb_promedio = Label(toplevel_resultados, text="Promedio: {}".format(promedio))
    lb_promedio.config(bg="bisque", font=("Times New Roman", 12))
    lb_promedio.place(x=10, y=240)
    if promedio < 32:
        lb_ad = Label(toplevel_resultados, text="Tu promedio está muy bajo, debes mejorar antes de quedar pfu o condicional")
        lb_ad.config(bg="bisque", font=("Times New Roman", 12))
        lb_ad.place(x=10, y=300)
    
# borrar
def borrar():
    messagebox.showinfo("Estado", "Los datos serán borrados")
    name.set("")
    generos_selected.set("") # borra el valor seleccionado en el combobox de género
    sangre_seleccionado.set("")
    edad.set("")
    codigo.set("")
    programa_selectec.set("")
    altura.set("")
    masa.set("")
    enfermedad_selecionada.set("")
    Fundamentos_de_Programación.set("")
    Calculo_1.set("")
    Algebra_lineal.set("")
    Quimica.set("")
    Deportes.set("")
    Taller_de_lenguage.set("")
    Catedra.set("")
    global promedio
    promedio = None
    
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
altura= StringVar()
masa = StringVar()
enfermedades = [  "Ninguna",  "Gripe",    "Resfriado",    "Bronquitis",    "Neumonía",    "Tuberculosis",    "VIH/SIDA",    "Hepatitis",    "Cáncer",    "Diabetes",    "Hipertensión",    "Asma",    "Alergias",    "Artritis",    "Obesidad",    "Anemia",    "Enfermedad de Parkinson",    "Alzheimer",    "Esquizofrenia",    "Depresión",    "Trastorno de ansiedad",    "Trastorno bipolar",    "Trastorno obsesivo-compulsivo",    "Trastorno de estrés postraumático",    "Trastornos alimentarios (anorexia, bulimia)",    "Trastornos del sueño (insomnio, apnea del sueño)"]
enfermedad_selecionada= StringVar()
Fundamentos_de_Programación=StringVar()
Calculo_1=StringVar() 
Algebra_lineal= StringVar()
Quimica= StringVar()
Deportes= StringVar()
Taller_de_lenguage=StringVar()
Catedra=StringVar()
vcmd = (ventana_principal.register(validate_number_input), '%P')
promedio=0

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
lb_c.config(bg= "bisque", fg="black", font=("Times New Roman", 18))
lb_c.place(x=15, y=90)

# caja de texto para la edad del estudiante
entry_c = Entry(frame_2, textvariable=edad, validate="key", validatecommand=vcmd)
entry_c.config(bg="white", fg="black", font=("Times New Roman", 18), width=6,)
entry_c.place(x=320,y=45)

# etiqueta para la edad del estudiane
lb_c = Label(ventana_principal, text = "Edad: ")
lb_c.config(bg ="bisque", fg="black", font=("Times New Roman", 18))
lb_c.place(x=260, y=130)

# caja de texto para codigo del estudiante
entry_c = Entry(frame_2, textvariable=codigo, validate="key", validatecommand=vcmd)
entry_c.config(bg="white", fg="black", font=("Times New Roman", 18), width=8,)
entry_c.place(x=100,y=45)

# etiqueta para el codigo del estudiante 
lb_c = Label(ventana_principal, text = "Codigo: ")
lb_c.config(bg = "Bisque", fg="black", font=("Times New Roman", 18))
lb_c.place(x=18, y=130)

# etiqueta para el programa del estudiante 
lb_c = Label(ventana_principal,textvariable=programa, text = "Programa : ")
lb_c.config(bg="bisque",fg="black", font=("Times New Roman", 18))
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
bt_r.place(x=330, y=470)

# boton para borrar
bt_r = Button(ventana_principal, text="Borrar", command=borrar)
bt_r.config(height=3, width=20)
bt_r.place(x=170, y=470)

bt_salir = Button(ventana_principal,text="Salir", command=salir)
bt_salir.config(height=3, width=20)
bt_salir.place(x=10, y=470)


#---------------------------------------------------
ventana_principal.mainloop()