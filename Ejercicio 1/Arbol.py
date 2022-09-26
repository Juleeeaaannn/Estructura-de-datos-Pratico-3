#Ejercicio Nº1: defina el objeto de datos árbol binario de búsqueda,
# especifique e implemente todos los métodos vistas en teoría.
from ast import If
from tkinter import N
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

    def Suprimir(self,elemento):
        nodo=self.Busqueda(self.__raiz,elemento)
        print(nodo.getElemento())
        if nodo.getSigD()==None and nodo.getSigI()==None:
            nodo=None
        else:
            if nodo.getSigD()!=None:
                aux=self.__raiz
                while(not self.Hijo(self.__raiz,nodo,aux)):
                    if aux < aux.getSigD():
                        aux=aux.getSigI()
                    else:
                        aux=aux.getSigD()
                aux.getSigD=nodo.getSigD()
                aux.getSigI=nodo.getSigI()

            elif nodo.getSigI()!=None:
                aux=self.__raiz
                while(not self.Hijo(self.__raiz,nodo,aux)):
                    if aux > aux.getSigI():
                        aux=aux.getSigD()
                    else:
                        aux=aux.getSigI()
                aux.getSigD=nodo.getSigD()
                aux.getSigI=nodo.getSigI()



    def Busqueda(self,nodo: Nodo,elemento):
        if nodo.getElemento() > elemento and nodo.getSigI() != None:
            self.Busqueda(nodo.getSigI(),elemento)

        elif nodo.getElemento() == elemento:
            print(f"elemento encontrado:{nodo.getElemento()}") 
            return nodo
        else:
            if nodo.getElemento() < elemento and nodo.getSigD() != None:
                self.Busqueda(nodo.getSigD(),elemento)
            elif nodo.getElemento() == elemento:
                print(f"elemento encontrado:{nodo.getElemento()}")
                return nodo
            else:
                print("Elemento no encontrado!")
           
    def Nivel(self,nodo,elemento,i=0):
        if nodo!=None:
            if nodo.getElemento() < elemento:
                self.Nivel(nodo.getSigD(),elemento,i+1)
            elif nodo.getElemento() > elemento:
                self.Nivel(nodo.getSigI(),elemento,i+1)
            else:
                print(f"el nodo es de nivel: {i}")
                return i
        else:
            print("nivel de elemento no encontrado")
        
    def Hoja(self):
        pass
    def Hijo(self,nodo:Nodo,X,Z):#evalua si x es descendiente directo de z
        if nodo!=None:
            if nodo==X:
                if nodo.getSigD() == Z or nodo.getSigI == Z:
                    print(f"si es hijo de {Z.getElemento()}")
            else:
                if nodo.getElemento() < nodo.getSigD.getElemento():
                    self.Hijo(nodo.getSigD,X,Z)
                else:
                    self.Hijo(nodo.getSigI,X,Z)
    def Padre(self,nodo:Nodo,Z,X):#evalua si x es descendiente directo de z
        if nodo!=None:
            if nodo==Z:
                if nodo.getSigD() == X or nodo.getSigI == X:
                    return True
            else:
                if nodo.getElemento() < nodo.getSigD.getElemento():
                    self.Hijo(nodo.getSigD,Z,X)
                else:
                    self.Hijo(nodo.getSigI,Z,X)
        else:
            return False

    # def Camino(self, nodo,nodoInicio,nodoFinal):
    #     if nodo!=None:
    #         if nodo == nodoInicio:
    #             print(f"{nodo.getElemento()}")
    #         else:
    #             if nodo!=nodoFinal:
                    
    def Altura(self,nodo:Nodo,i=0):
        if nodo!=None:
            aux1=self.Altura(nodo.getSigI(),i+1)
            aux2=self.Altura(nodo.getSigD(),i+1)
            return max(aux1,aux2)
        else:
            return i
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
    arbol.InOrden(arbol.Raiz())
    print("---")
    arbol.Suprimir("2")
    arbol.InOrden(arbol.Raiz())
    # arbol.Nivel(arbol.Raiz(),"3")
    # print(arbol.Altura(arbol.Raiz()))
    # arbol.Hijo(arbol.Raiz(),)