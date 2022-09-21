#Ejercicio Nº1: defina el objeto de datos árbol binario de búsqueda,
# especifique e implemente todos los métodos vistas en teoría.
from Nodo import Nodo
class Arbol:
    __raiz=None
    def __init__(self):
        self.__raiz=None
    def Insertar(self,nodo,elemento):
        if(nodo==None):
            aux=Nodo(elemento)
            self.__raiz=aux
        else:
            if nodo.getElemento()==elemento:
                print("Elemento ya existente")
            else:
                if nodo.getElemento() < elemento and nodo.getSigD()!=None:
                    self.Insertar(nodo.getSigD(),elemento)

                elif nodo.getElemento() < elemento and nodo.getSigD()==None:
                    aux=Nodo(elemento)
                    nodo.setSigD(aux)

                else:
                    if nodo.getElemento() > elemento and nodo.getSigI()!=None:
                        self.Insertar(nodo.getSigI(),elemento)

                    elif nodo.getElemento() > elemento and nodo.getSigI()==None:
                        aux=Nodo(elemento)
                        nodo.setSigI(aux)

    def Suprimir(self):
        pass
    def Busqueda(self,nodo: Nodo,elemento):
        if nodo.getElemento() > elemento and nodo.getSigI() != None:
            self.Busqueda(nodo.getSigI(),elemento)

        elif nodo.getElemento() == elemento:
            print(f"elemento encontrado:{nodo.getElemento()}") 
        
        else:
            if nodo.getElemento() < elemento and nodo.getSigD() != None:
                self.Busqueda(nodo.getSigD(),elemento)
            elif nodo.getElemento() == elemento:
                print(f"elemento encontrado:{nodo.getElemento()}")
                return nodo
            else:
                print("Elemento no encontrado!")
           
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
    def InOrden(self,nodo):
        if nodo!=None:
            self.InOrden(nodo.getSigI())
            print(nodo.getElemento())
            self.InOrden(nodo.getSigD())

    def PreOrden(self,nodo):
        if nodo!=None:
            print(nodo.getElemento())
            self.PreOrden(nodo.getSigI())
            self.PreOrden(nodo.getSigD())
    def PostOrden(self,nodo):
        if nodo!=None:
            self.PostOrden(nodo.getSigI())
            self.PostOrden(nodo.getSigD())
            print(nodo.getElemento())
    def Raiz(self):
        return self.__raiz
if __name__ =='__main__':
    arbol=Arbol()
    arbol.Insertar(arbol.Raiz(),"2")
    arbol.Insertar(arbol.Raiz(),"1")
    arbol.Insertar(arbol.Raiz(),"4")
    arbol.Insertar(arbol.Raiz(),"3")
    print("Pre orden")
    arbol.PreOrden(arbol.Raiz())
    print("In orden")
    arbol.InOrden(arbol.Raiz())
    print("Post orden")
    arbol.PostOrden(arbol.Raiz())
    arbol.Busqueda(arbol.Raiz(),"5")