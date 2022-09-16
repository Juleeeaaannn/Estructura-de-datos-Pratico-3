#Ejercicio Nº1: defina el objeto de datos árbol binario de búsqueda,
# especifique e implemente todos los métodos vistas en teoría.
from pickle import NONE
from Nodo import Nodo
class Arbol:
    __raiz=None
    def __init__(self):
        self.__raiz=None
    def Vacio(self):
        return (self.__raiz==None)
    def Insertar(self,nodo,elemento):
        if(nodo==None):
            aux=Nodo(elemento)
            self.__raiz=aux
        else:
            if nodo.getElemento()==elemento:
                print("Elemento ya existente")
            else:
                if nodo.getSigD() != None:
                    
                    self.Insertar(nodo.getSigD(),elemento)
                
                elif nodo.getSigD() == None:
                    
                    aux=Nodo(elemento)
                    nodo.setSigD(aux)

                else:
                    if nodo.getSigI() != None:
                        self.Insertar(nodo.getSigI(),elemento)
                    else:
                        aux=Nodo(elemento)
                        nodo.setSigI(aux)
    def Suprimir(self):
        pass
    def Busqueda(self):
        pass
    def Nivel(self):
        pass
    def Hoja(self):
        pass
    def Hijo(self):
        pass
    def Padre(self):
        pass
    def Camino(self):
        pass
    def Altura(self):
        pass
    def InOrden(self):
        pass
    def PreOrden(self,nodo):
        if nodo!=None:
            print(nodo.getElemento())
            self.PreOrden(nodo.getSigI())
            self.PreOrden(nodo.getSigD())
    def PostOrden(self,A):
        pass
    def Raiz(self):
        return self.__raiz
if __name__ =='__main__':
    arbol=Arbol()
    arbol.Insertar(arbol.Raiz(),"A")
    arbol.Insertar(arbol.Raiz(),"B")
    arbol.PreOrden(arbol.Raiz())