from tkinter import *
raiz = Tk()
raiz.title("Hola Mundo")
raiz.iconbitmap("Iconos\mario_super_bros_icon_232936.ico") #Esta linea ubica el icono en la ventana.
raiz.geometry("1080x720") #Esto sirve para escalar el tamaño de la ventana (Ancho Alto)
raiz.resizable(1,1) #Esto es (true and false), sirve para habilitar la redimension
raiz.config(bg="blue") #Configuracion de la ventana("bg=background",...)
raiz.mainloop()
