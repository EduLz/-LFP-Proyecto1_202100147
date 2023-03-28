import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.constants import END
from automata import Automata
from Operacion import Operacion
import graphviz
import webbrowser
from graphviz import Digraph
import re
# Crea la ventana principal
root = tk.Tk()
root.title("Mi ventana")
root.geometry("300x200")
root.configure(bg='gray')
archivo_seleccionado = ''
grafo_global = Digraph(comment='Grafo global de operaciones', format='png')
style = ttk.Style()
ttk.Style().configure("Boton.TButton", background="#4CAF50", foreground="#FFFFFF")
def cerrar_ventana2():
        root.destroy() 
                
def abrir_archivo():
    # Crea una nueva ventana emergente
    new_window = tk.Toplevel()
    new_window.title("Ingresar texto")
    new_window.geometry("600x400")
    new_window.configure(bg='gray')
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
    button2 = tk.Button(new_window, text="Seleccionar Archivo",bg="#007bff", fg="#fff", font=("Arial", 10), width=15, command=seleccionar_archivo)
    button2.place(x=450, y=10)
    def guardar_archivo():
        global archivo_seleccionado
        if archivo_seleccionado:
            with open(archivo_seleccionado, 'w') as file:
                contenido = text_area.get("1.0", "end-1c")
                file.write(contenido)
    button3 = tk.Button(new_window, text="Guardar", bg="#007bff", fg="#fff", font=("Arial", 10), width=15, command=guardar_archivo)
    button3.place(x=450, y=40)
    def guardar_como():
        global archivo_seleccionado
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                contenido = text_area.get("1.0", "end-1c")
                file.write(contenido)
                archivo_seleccionado = file_path
    button4 = tk.Button(new_window, text="Guardar como", bg="#007bff", fg="#fff", font=("Arial", 10), width=15, command=guardar_como)
    button4.place(x=450, y=70)
    def boton_analizador():
        global archivo_seleccionado
        autom = Automata()
        cadena = open(archivo_seleccionado, 'r').read()
        resultado = autom.analizar(cadena, Operacion(''))
        if len(resultado[2])>0:    
            contador = 0
            cadenatodo='{\n'
            for i in resultado[2]:
                if len(resultado[2])-1==contador:
                    cadenatodo+=i.generar_cadena(contador)+'\n'
                else:
                    cadenatodo+=i.generar_cadena(contador)+',\n'    
                contador+=1  
            cadenatodo+='}\n'
            f = open("archivo_errores.txt", "w")
            f.write(cadenatodo)
            f.close()
        #autom.imprimir_tokens()    
        if autom.estado_actual in autom.estados_aceptacion:
            for oper in resultado[1]:
                resultado_operacion = oper.operar()
                print(resultado_operacion[0], "=", resultado_operacion[1])
                grafo = oper.generar_grafo()
                nombre_archivo = f'{resultado_operacion[0]}_{resultado_operacion[1]}'
                nombre_archivo = re.sub(r'[^\w\-_\. ]', '', str(resultado_operacion[1]))
                grafo.render(f'grafosgenerados/grafo_operacion_{nombre_archivo}', format='png', view=True)
        else:
            print(resultado[2])
            print("Cadena no aceptada por el autómata")
        

    button6 = tk.Button(new_window, text="Analizar", bg="#007bff", fg="#fff", font=("Arial", 10),width=15, command=boton_analizador)
    button6.place(x=450, y=110)
    def cerrar_ventana():
        text_area.delete(1.0, END)
        new_window.destroy()
    button9 = tk.Button(new_window, text="Salir", bg="#007bff", fg="#fff", font=("Arial", 10), width=15, command=cerrar_ventana)
    button9.place(x=450, y=140)     
#Botones
label = tk.Label(root, text="Archivo",bg="green", fg="#fff", font=("Arial", 10))
label.place(x=40,y=1)
button1 = tk.Button(root, text="Abrir Archivo", bg="#007bff", fg="#fff", font=("Arial", 10),width=15, command=abrir_archivo)
button1.place(x=1, y=31)
def abrir_errores():
    window_errores = tk.Toplevel()
    window_errores.title("Errores generados")
    window_errores.geometry("550x400")
    text_area_errores = tk.Text(window_errores, width=40, height=20, font="Arial")
    text_area_errores.place(x=50, y=10)
    file_path = 'D:\\USAC\\2023\\Primer Semestre\\LFP\\LAB-LFP\\Proyecto1\\Proyecto1\\archivo_errores.txt'       
    if file_path:
        with open(file_path, 'r') as file:
            contenido = file.read()
            text_area_errores.delete(1.0, END)
            text_area_errores.insert(END, contenido)
    def cerrar_ventana():
        text_area_errores.delete(1.0, END)
        window_errores.destroy()
    buttonErrores = tk.Button(window_errores, text="Salir", width=15, command=cerrar_ventana)
    buttonErrores.place(x=425, y=10)
button5 = tk.Button(root, text="Errores",bg="#007bff", fg="#fff", font=("Arial", 10), width=15, command=abrir_errores)
button5.place(x=1, y=61)
button6 = tk.Button(root, text="Salir", bg="#007bff", fg="#fff", font=("Arial", 10),width=15, command=cerrar_ventana2)
button6.place(x=1, y=91)
label2 = tk.Label(root, text="Ayuda",bg="green", fg="#fff", font=("Arial", 10))
label2.place(x=200,y=1)
def abrir_manualusuario():
    ruta_archivo = "D:\\USAC\\2023\\Primer Semestre\\LFP\\LAB-LFP\\Proyecto1\\Proyecto1\\Documentacion\\Manual de usuario.pdf"
    webbrowser.open_new(ruta_archivo)
button7 = tk.Button(root, text="Manual de Usuario", bg="#007bff", fg="#fff", font=("Arial", 10),width=15, command=abrir_manualusuario)
button7.place(x=150, y=31)
def abrir_manualtecnico():
    ruta_archivo = "D:\\USAC\\2023\\Primer Semestre\\LFP\\LAB-LFP\\Proyecto1\\Proyecto1\\Documentacion\\Manual tecnico.pdf"
    webbrowser.open_new(ruta_archivo)
button8 = tk.Button(root, text="Manual Tecnico", bg="#007bff", fg="#fff", font=("Arial", 10),width=15, command=abrir_manualtecnico)
button8.place(x=150, y=61)

 
        
        
# Inicia el loop principal
root.mainloop()
