from Nodo import Nodo 
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else: 
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
    
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else: 
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()
        
    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return
    
    def modificar(self, datoActual, datoNuevo):
        actual = self.cabeza
        while actual:
            if actual.dato == datoActual:
                actual.dato = datoNuevo
                return
            actual = actual.siguiente
                
    def eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else: 
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                return
            actual = actual.siguiente
            
    