import sys
import tkinter as tk
import tkinter.scrolledtext as scroll
import tkinter.filedialog as filed

import os

import tkinter.messagebox as mensaje
from tkinter import *
import tkinter.ttk as ttk
#from lectura import *
#from lectura import *
import lectura as lec

class Vtabla:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tabla de tokens")
        self.ventana.geometry('1000x700')
        self.ventana['bg'] = 'red'

       
        encabezados = ('No.', 'TOKEN', 'LEXEMA')
        self.tabla = ttk.Treeview(self.ventana, columns=encabezados,show='headings', height=20) # height es cuantas filas se van a mostrar

        
        # configurar encabezados
        self.tabla.heading('No.', text='Numero atomico')
        self.tabla.column('No.', anchor=tk.CENTER)
        self.tabla.heading('TOKEN', text='simbolo')
        self.tabla.column('TOKEN', anchor=tk.CENTER)
        self.tabla.heading('LEXEMA', text='nombre')
        self.tabla.column('LEXEMA', anchor=tk.CENTER)
        
       
        
        # estilo de self.tabla
        estilo = ttk.Style(self.tabla)
        estilo.theme_use('classic')
        
         # Configurar encabezados
        estilo.configure('Treeview.Heading',foreground='red',font=('Calibri', 20, 'bold'))

        #personas = [{'Nombre':'Wilson', 'Color':'Rojo'},{'Nombre':'Carmen', 'Color':'Verde'},{'Nombre':'Arelis', 'Color':'Azul'},{'Nombre':'Cecilia', 'Color':'Amarillo'} ]
        
        elementos_q,maquinas= lec.leer_xml()
        print(elementos_q)
        #lista = lectura.leer_xml()
        contador = 1
        for elemento in elementos_q:
            # Los datos tienen que estar en el mismo orden y cantidad que indican las columnas
            # cada iteracion llenara una fila
            
            numero =  elemento["numeroAtomico"]
            simbolo = elemento["simbolo"]
            nombre = elemento["nombreElemento"]
            
            #lexema = token.valor
            informacion = [numero,simbolo,nombre]
            # para agregar una fila se usa la funcion insert de la tabla
            self.tabla.insert('','end',values=informacion)
            contador += 1
            print(elemento)
            
        self.tabla.place(x=99, y=150)
    
       
        self.ventana.mainloop()


