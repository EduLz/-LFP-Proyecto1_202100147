import tkinter as tk
from tkinter import filedialog
from tkinter.constants import END
from automata import Automata
from Operacion import Operacion
# Crea la ventana principal
root = tk.Tk()
root.title("Mi ventana")
root.geometry("300x200")
archivo_seleccionado = ''
def cerrar_ventana2():
        root.destroy() 
                
def abrir_archivo():
    # Crea una nueva ventana emergente
    new_window = tk.Toplevel()
    new_window.title("Ingresar texto")
    new_window.geometry("600x400")
    text_area = tk.Text(new_window, width=40, height=20, font="Arial")
    text_area.place(x=50, y=10)
    def seleccionar_archivo():
            file_path = filedialog.askopenfilename()
            
            if file_path:
                with open(file_path, 'r') as file:
                    contenido = file.read()
                    text_area.delete(1.0, END)
                    text_area.insert(END, contenido)
                    global archivo_seleccionado
                    archivo_seleccionado = file_path
    button2 = tk.Button(new_window, text="Seleccionar Archivo", width=15, command=seleccionar_archivo)
    button2.place(x=450, y=10)
    def guardar_archivo():
        global archivo_seleccionado
        if archivo_seleccionado:
            with open(archivo_seleccionado, 'w') as file:
                contenido = text_area.get("1.0", "end-1c")
                file.write(contenido)
    button3 = tk.Button(new_window, text="Guardar", width=15, command=guardar_archivo)
    button3.place(x=450, y=40)
    def guardar_como():
        global archivo_seleccionado
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                contenido = text_area.get("1.0", "end-1c")
                file.write(contenido)
                archivo_seleccionado = file_path
    button4 = tk.Button(new_window, text="Guardar como", width=15, command=guardar_como)
    button4.place(x=450, y=70)
    #FALTA EL ANALIZADOR
    def boton_analizador():
        global archivo_seleccionado
        autom = Automata()
        cadena = open(archivo_seleccionado, 'r').read()
        resultado = autom.analizar(cadena, Operacion(''))

        #autom.imprimir_tokens()

        if autom.estado_actual in autom.estados_aceptacion:
            for oper in resultado[1]:
                resultado = oper.operar()
                print(resultado[0], "=", resultado[1])
    
    button6 = tk.Button(new_window, text="Analizar", width=15, command=boton_analizador)
    button6.place(x=450, y=110)
    def cerrar_ventana():
        text_area.delete(1.0, END)
        new_window.destroy()
    button9 = tk.Button(new_window, text="Salir", width=15, command=cerrar_ventana)
    button9.place(x=450, y=140)     
#Botones
label = tk.Label(root, text="Archivo")
label.place(x=40,y=1)
button1 = tk.Button(root, text="Abrir Archivo", width=15, command=abrir_archivo)
button1.place(x=1, y=31)
button5 = tk.Button(root, text="Errores", width=15)
button5.place(x=1, y=61)
button6 = tk.Button(root, text="Salir", width=15, command=cerrar_ventana2)
button6.place(x=1, y=91)
label2 = tk.Label(root, text="Ayuda")
label2.place(x=200,y=1)
button7 = tk.Button(root, text="Manual de Usuario", width=15)
button7.place(x=150, y=31)
button8 = tk.Button(root, text="Manual Tecnico", width=15)
button8.place(x=150, y=61)

 
        
        
# Inicia el loop principal
root.mainloop()
