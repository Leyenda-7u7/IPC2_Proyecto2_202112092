from xml.dom import minidom
from prueba import *
import elemen as ele
import tabla

elementos_quimicos = []
maquinas_con_pines = []

def leer_xml():
    # abrir el archivo XML
    doc = minidom.parse("Entrada_Ejemplo_P2.xml")

    # obtener el elemento principal
    CONFIG = doc.getElementsByTagName("CONFIG")[0]

    # obtener la lista de elementos
    listaElementos = CONFIG.getElementsByTagName("listaElementos")[0]
    elementos = listaElementos.getElementsByTagName("elemento")

    # construir lista de elementos químicos
    elementos_quimicos = []
    for elemento in elementos:
        numeroAtomico = elemento.getElementsByTagName("numeroAtomico")[0].childNodes[0].data
        simbolo = elemento.getElementsByTagName("simbolo")[0].childNodes[0].data
        nombreElemento = elemento.getElementsByTagName("nombreElemento")[0].childNodes[0].data
        #elemento_quimico = ele.Elemento(numeroAtomico,simbolo,nombreElemento)
        elemento_quimico = {
            "numeroAtomico": numeroAtomico,
            "simbolo": simbolo,
            "nombreElemento": nombreElemento
        }
        elementos_quimicos.append(elemento_quimico)
        #tabla.Vtabla(elementos_quimicos)

    # obtener la lista de máquinas
    listaMaquinas = CONFIG.getElementsByTagName("listaMaquinas")[0]
    maquinas = listaMaquinas.getElementsByTagName("Maquina")

    # construir lista de máquinas con sus pines
    maquinas_con_pines = []
    for maquina in maquinas:
        nombre = maquina.getElementsByTagName("nombre")[0].childNodes[0].data
        numPines = int(maquina.getElementsByTagName("numeroPines")[0].childNodes[0].data)
        numElementos = int(maquina.getElementsByTagName("numeroElementos")[0].childNodes[0].data)

        # obtener la lista de pines
        pines = maquina.getElementsByTagName("pin")
        lista_pines = []

        # construir lista de elementos de cada pin
        for pin in pines:
            elementos_pin = []
            elementosPin = pin.getElementsByTagName("elemento")
            for elementoPin in elementosPin:
                elemento = elementoPin.childNodes[0].data
                elementos_pin.append(elemento)
            lista_pines.append(elementos_pin)

        maquina_con_pines = {
            "nombre": nombre,
            "numPines": numPines,
            "numElementos": numElementos,
            "pines": lista_pines
        }
        maquinas_con_pines.append(maquina_con_pines)

    # devolver lista de elementos químicos y lista de máquinas con pines
    return elementos_quimicos, maquinas_con_pines




