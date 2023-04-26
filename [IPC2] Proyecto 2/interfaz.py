from fileinput import filename
import os
import subprocess
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter.tix import Tree
from tkinter import Tk
from tkinter import *
from tkinter import ttk
import tkinter as tk
#from lectura import *
import lectura
import os 

import tabla

class Pantalla_Principal():
    
        
    def __init__(self):
        self.PP = Tk()
        self.PP.title("Pantalla Principal")
        self.centrar(self.PP, 900, 900)
        self.PP.configure(bg = "#102027")
        self.pantalla_1()
        
        
    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla= r.winfo_screenwidth()
        w = (anchura_pantalla // 2) - (ancho//2)
        e = (altura_pantalla // 2) - (alto//2)
        r.geometry(f"+{w}+{e}")
        
        
    def pantalla_1(self):
        self.Frame = Frame()
        self.Frame.config(bg ="tan")
        self.Frame.config(bd=15)
        self.Frame.config(relief="sunken")  #Le da el borde
        self.Frame.config(cursor="hand2")
        self.Frame.pack(side=tk.LEFT, fill="x") 
        self.Frame.configure(height=790, width=900)

        LabelFrame
        Button(self.Frame, command=self.abrir_archivo ,text="Abrir Archivo", font=("Arial Black", 16), fg="gray99", bg="dim gray", width=10).place(x=100, y=50)
        Button(self.Frame, command= self.tabla ,text="Tabla", font=("Arial Black", 16), fg="gray99", bg="dim gray", width=10).place(x=100, y=130)
        Button(self.Frame, command= self.grafica_pines,text="Grafica Pines", font=("Arial Black", 16), fg="gray99", bg="dim gray", width=10).place(x=320, y=130)
        Button(self.Frame, command= self.abrir_usuario,text="Ensayo", font=("Arial Black", 16), fg="gray99", bg="dim gray", width=10).place(x=500, y=130)
        
        
        Button(self.Frame, command=self.guardar_como ,text="Guardar Como", font=("Arial Black", 16),fg="gray99", bg="dim gray", width=11).place(x=300, y=50)
        
        Button(self.Frame ,text="Elementos", command=self.ejecutar, font=("Arial Black", 16), fg="gray99", bg="dim gray", width=8).place(x=500, y=50)
        
        Button(self.Frame, text="Cerrar Ventana", command=self.PP.destroy, font=("Arial Black", 16), fg="gray99", bg="dim gray", width=12).place(x=650, y=50)

        Button(self.Frame,text="Ayuda", command=self.ayuda, font=("Arial Black", 16), fg="gray99", bg="dim gray", width=10).place(x=700, y=130)
        
        self.text = Text(self.Frame, font=("Arial", 15), fg="black", width=45, height=8)
        self.text.place(x=200, y=350)
        
        self.resultado_text = Text(self.Frame, font=("Arial", 15), fg="black", width=30, height=6)
        self.resultado_text.place(x=300, y=600)
        

        self.Frame.mainloop() 
    
    def abrir_usuario(self):
        os.startfile("Ensayo IPC2.pdf")    

    def abrir_archivo(self):
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo', filetypes=[('Archivos', f'*.xml')])
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                                            
        except: 
            print("Error, no se ha seleccionado ningun archivo")
            return
        
        self.texto = x
        self.text.insert('1.0', x)
        
    def ejecutar(self):
        # llamar a la función leer_xml()
        mensaje = lectura.leer_xml()
        # mostrar el resultado en el text area
        self.resultado_text.insert(tk.END, mensaje)
        self.grafica()

    def tabla(self):
        tabla.Vtabla()
        
    def guardar_como(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            with open(filename, "w", encoding="utf-8") as outfile:
                outfile.write(self.resultado_text.get("1.0", "end-1c"))

    def grafica_pines(self):
        
        elemntos,maquinas = lectura.leer_xml()
        buffer = ""
        file = open('maquinas.dot', 'w')
        buffer += "digraph G { bgcolor=\"white\" \n"
        buffer += "a0 [shape = \"none\", label=< \n"
        buffer += "<TABLE border=\"0\" cellspacing=\"2\" cellpadding=\"5\" bgcolor=\"white\"> \n"
        buffer += "<TR>\n"
        buffer += "<TD colspan=\"3\" border=\"1\" > Informacion de maquinas </TD> \n"
        buffer += "</TR>\n"
        
        buffer += "<TR>\n"
        buffer += "<TD border=\"1\" > Maquina </TD> \n"
        buffer += "<TD border=\"1\" > Pines </TD> \n"
        buffer += "<TD border=\"1\" > Elementos </TD> \n"
        buffer += "</TR>\n"
        
        for maquina in maquinas:
            buffer += "<TR>\n" 
            buffer += "<TD border=\"1\">"
            buffer +=  maquina["nombre"]
            buffer += "</TD> \n"
            
            buffer += "<TD border=\"1\">"
            buffer += str(maquina["numPines"])
            buffer += "</TD> \n"
            
            buffer += "<TD border=\"1\">"
            buffer += str(maquina["numElementos"])
            buffer += "</TD> \n"
            
            buffer += "</TR>\n" 
            
            buffer += "<TR>\n"
            buffer += "<TD colspan=\"3\" border=\"1\" > Pines </TD> \n"
            buffer += "</TR>\n"
            for pin in maquina["pines"]:
                for pin_actual in pin:
                    
                    
                    buffer += "<TR>\n"
                    buffer += "<TD colspan=\"3\" border=\"1\" > "+pin_actual+" </TD> \n"
                    buffer += "</TR>\n"
                

        buffer +=  "</TABLE>>]; \n" 
        buffer +=  "}\n"
        file.write(buffer)
        file.close()
        os.system('dot -Tpng maquinas.dot -o maquina.png')
        os.startfile("maquina.png")
    
    
    def grafica(self):
        
        grafica= ""
        grafica += 'digraph {'
        grafica += 'graph [pad="0.5", nodesep="0.5", ranksep="2", splines="ortho"];'
        grafica += 'node [shape=plain]'
        grafica += 'rankdir=LR;'


        grafica += 'Foo [label=<'
        grafica += '<table border="0" cellborder="1" cellspacing="0">'
        for elemento in lectura.leer_xml():
            
            grafica += '<tr>  <td><i>'+ str(elemento) +'</i></td> <td> two </td>   </tr>'
            grafica += '<tr>  <td><i>'+ str(elemento) +'</i></td> <td> two </td>   </tr>'
            grafica += '<tr>  <td><i>'+ str(elemento) +'</i></td> <td> two </td>   </tr>'
            #grafica += '<tr>  <td port="1">one</td> <td> two </td></tr>
        

        grafica += '</table>>];'


        
        grafica += '}'
        
        docu = open('Grafica.dot', 'w', encoding='utf-8') 
        docu.write(grafica)
        docu.close()
        
        lista =["dot.exe","-Tpng","Grafica.dot","-o","Grafica.png"]
            
        subprocess.run(lista)
        os.startfile("Grafica.png")
        
    def ayuda(self):
        os.startfile("informacion.pdf") 
        
r = Pantalla_Principal()


