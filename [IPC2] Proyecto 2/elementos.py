from lectura import *

# leer el archivo XML y guardar los resultados en variables
elementos_quimicos, maquinas_con_pines = leer_xml()

# usar las variables para crear compuestos

class ElementoQuimico:
    def __init__(self, numeroAtomico, simbolo, nombre):
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.nombre = nombre

class Pin:
    def __init__(self):
        self.elemento = None
        self.posicion = 0

    def avanzar(self):
        self.posicion += 1

    def retroceder(self):
        self.posicion -= 1

    def esperar(self):
        pass

    def fusionar(self, elemento):
        if self.elemento is None:
            self.elemento = elemento
        else:
            print("Este pin ya contiene un elemento químico")

class Maquina:
    def __init__(self, nombre, numPines):
        self.nombre = nombre
        self.pines = [Pin() for i in range(numPines)]
        self.elementos = set()

    def fusionar(self, index):
        pin_actual = self.pines[index]
        if pin_actual.elemento is not None:
            if pin_actual.posicion == len(self.pines) - 1:
                compuesto = self._crear_compuesto()
                print("Compuesto creado:", compuesto)
                self.elementos.clear()
                for pin in self.pines:
                    pin.elemento = None
                    pin.posicion = 0
            else:
                pin_siguiente = self.pines[index + 1]
                if pin_siguiente.elemento is None:
                    pin_siguiente.elemento = pin_actual.elemento
                    pin_actual.elemento = None
                    pin_actual.avanzar()
                    pin_siguiente.avanzar()
                    self.elementos.add(pin_siguiente.elemento)
                else:
                    print("El pin siguiente ya contiene un elemento químico")
        else:
            print("Este pin no contiene ningún elemento químico")

    def _crear_compuesto(self):
        elementos = sorted(list(self.elementos), key=lambda x: x.numeroAtomico)
        nombre_compuesto = ""
        for elemento in elementos:
            nombre_compuesto += elemento.simbolo
        return nombre_compuesto
