# Ejercicio Nº3: Usando el mismo objeto de datos del ej. 1, implemente una función para c/u de los siguientes incisos:
# a) Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por
# teclado; éste puede o no existir en el árbol.
# b) mostrar la cantidad de nodos del árbol en forma recursiva.
# c) Mostrar la altura de un árbol.
# d) Mostrar los sucesores de un nodo ingresado previamente por teclado.
from Nodo import Nodo

class Arbol:
    __raiz=None

    def __init__(self):
        self.__raiz=None

    def Insertar(self,nodo,elemento): #bien
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

    def grado (self, nodo):
        grado = 2
        if nodo.getSigD() == None and nodo.getSigI() == None: 
            grado = 0
        elif nodo.getSigI() != None and nodo.getSigD() == None or nodo.getSigI() == None and nodo.getSigD() != None: #evalua si tiene hijo por izq
            grado = 1
        return grado

    def Suprimir(self,elemento): 
        self.__Suprimir(self.__raiz,self.__raiz,elemento)

    def __Suprimir(self,nodo,nodoP,elemento):   #revision
        if nodo==None:
            print("Lista Vacia")
        else:
            if nodo.getElemento() < elemento and nodo.getSigD()!=None:
                nodoP=nodo
                self.__Suprimir(nodo.getSigD(),nodoP,elemento)
            
            else:
                if nodo.getElemento() > elemento and nodo.getSigI()!=None:
                    nodoP=nodo
                    self.__Suprimir(nodo.getSigI(),nodoP,elemento)
                    
                elif nodo.getElemento()==elemento :#pregunta si tiene una hoja por la izquierda
                    if self.grado(nodo) == 0:
                        if nodoP.getSigD()==nodo:
                            nodoP.setSigD(None)
                            print("es nodo Derecho")
                        else:
                            nodoP.setSigI(None)
                            print("es nodo Izquierdo")
                            print("grado = 0")
                    elif self.grado(nodo) == 1:
                        if nodo.getSigD()!=None:
                            nodoP.setSigD(nodo.getSigD())
                            nodo=None
                        elif nodo.getSigI()!=None:
                            nodoP.setSigD(nodo.getSigD())
                            nodo=None
                            print("grado = 1")
                    else:
                        aux=nodo.getSigI()
                        if aux.getSigD()==None: 
                            nodo.setElemento(aux.getElemento())
                            nodo.setSigI(None)
                        else:
                            ant=nodo.getSigI() #al padre le asignamos la derecha siguiente del hijo
                            while aux.getSigD() != None:
                                ant=aux
                                aux = aux.getSigD()
                            nodo.setElemento(aux.getElemento())
                            ant.setSigD(aux.getSigI())
                            aux=None
                            #aux1 = aux.getSigD()    
                            #self.__Suprimir(aux,aux.getSigD(),aux1.getElemento())
                        print("grado = 2")

    def Nivel(self,nodo,elemento,i=0):  #bien
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
    
    def _obtener(self,clave,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.getElemento() == clave:
            return nodoActual
        elif clave < nodoActual.getElemento():
            return self._obtener(clave,nodoActual.getSigI())
        else:
            return self._obtener(clave,nodoActual.getSigD())
        
    def Hoja(self, nodo, elemento): #faltaa
        if nodo != None:
            hojita = self._obtener(elemento, nodo)
            if hojita.getSigD() == None and hojita.getSigI() == None:
                print("el nodo es hoja")
            else:
                print("el nodo no es hoja")
        else:
            print("el arbol no tiene nodos")

                
    def Hijo(self,nodo:Nodo,X,Z):#evalua si x es descendiente directo de z #bien
        if nodo!=None:
            if nodo==X:
                if nodo.getSigD() == Z or nodo.getSigI == Z:
                    print(f"si es hijo de {Z.getElemento()}")
            else:
                if nodo.getElemento() < nodo.getSigD.getElemento():
                    self.Hijo(nodo.getSigD,X,Z)
                else:
                    self.Hijo(nodo.getSigI,X,Z)

    def Padre(self,nodo:Nodo,Z,X):#evalua si x es descendiente directo de z #revisar
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

    def Camino(self,nodoInicio,nodoFinal):
        lista=[]
        self.__Camino(self.__raiz,nodoInicio,nodoFinal,lista)

    def __Camino(self, nodo,nodoInicio,nodoFinal,lista):
        if nodo!=None:
            if nodo.getElemento() > nodoInicio and nodoInicio!=-1:
                self.__Camino(nodo.getSigI(),nodoInicio,nodoFinal,lista)
            elif nodo.getElemento() < nodoInicio and nodoInicio!=-1:
                self.__Camino(nodo.getSigD(),nodoInicio,nodoFinal,lista)
            else:
                lista.append(nodo.getElemento())
                if nodo.getElemento() > nodoFinal:
                    self.__Camino(nodo.getSigI(),-1,nodoFinal,lista)
                elif nodo.getElemento() < nodoFinal:
                    self.__Camino(nodo.getSigD(),-1,nodoFinal,lista)
                else:
                    print(lista)
    

    def Altura(self,nodo:Nodo,i=0): #revisar
        if nodo!=None:
            aux1 = self.Altura(nodo.getSigI(),i+1)
            aux2 = self.Altura(nodo.getSigD(),i+1)
            return max(aux1,aux2)
        else:
            return i

    def InOrden(self,nodo):  #bien
        if nodo!=None:
            self.InOrden(nodo.getSigI())
            print(nodo.getElemento())
            self.InOrden(nodo.getSigD())

    def PreOrden(self,nodo):  #bien
        if nodo!=None:
            print(nodo.getElemento())
            self.PreOrden(nodo.getSigI())
            self.PreOrden(nodo.getSigD())

    def PostOrden(self,nodo): #bien
        if nodo!=None:
            self.PostOrden(nodo.getSigI())
            self.PostOrden(nodo.getSigD())
            print(nodo.getElemento())

    def Raiz(self): #bien
        return self.__raiz
    # a) Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por
    # teclado; éste puede o no existir en el árbol.
    def NodoPyH(self,elemento):
        self.__NodoPyH(self.__raiz,self.__raiz,elemento)
        
    def __NodoPyH(self,nodo,padre,elemento):
        if nodo!=None:
            if nodo.getElemento() > elemento:
                self.__NodoPyH(nodo.getSigI(),nodo,elemento)
            elif nodo.getElemento() < elemento:
                self.__NodoPyH(nodo.getSigD(),nodo,elemento)
            elif nodo.getElemento()==elemento:
                if padre.getSigD()==nodo and padre.getSigI()!=None:
                    padre=padre.getSigI()
                    print(padre.getElemento())
                    print(nodo.getElemento())
                elif padre.getSigI()==nodo and padre.getSigD()!=None:
                    padre=padre.getSigI()
                    print(padre.getElemento())
                    print(nodo.getElemento())
                else:
                    print(nodo.getElemento())
                    print("No tiene hermanos!")

    def CantidadNodos(self,nodo:Nodo,i=0): 
        if nodo!=None:
            aux1 = self.Altura(nodo.getSigI(),i+1)
            aux2 = self.Altura(nodo.getSigD(),i+1)
            return aux1 + aux2
        else:
            return i
    
    def Sucesores (self, nodo, elemento):
        if nodo != None:
            nodito = self._obtener(elemento, nodo)
            if nodito.getSigI() != None and nodito.getSigD() != None:
                print("Tiene sucesores")
                print("a la izquiera: ", nodito.getSigI().getElemento(), "a la derecha: ", nodito.getSigD().getElemento())
            elif nodito.getSigI() == None and nodito.getSigD() != None:
                print("Solo tiene sucesor a la derecha: ", nodito.getSigD().getElemento())
            elif nodito.getSigI() != None and nodito.getSigD() == None:
                print("Solo tiene sucesor a la izquiera: ", nodito.getSigI().getElemento())
            else:
                print("No tiene sucesores")


if __name__ =='__main__':
    arbol=Arbol()
    arbol.Insertar(arbol.Raiz(),6)
    arbol.Insertar(arbol.Raiz(),2)
    arbol.Insertar(arbol.Raiz(),8)
    arbol.Insertar(arbol.Raiz(),1)
    arbol.Insertar(arbol.Raiz(),4)
    arbol.Insertar(arbol.Raiz(),3)
    #arbol.Insertar(arbol.Raiz(),79)
    print("-------------- SUCESORES --------------------")
    arbol.Sucesores(arbol.Raiz(), 4)
    
    #print(arbol.CantidadNodos(arbol.Raiz()))
    # arbol.Suprimir(4)
    # arbol.InOrden(arbol.Raiz())
    # print("---------------------")
    # arbol.Suprimir(2)
    # arbol.InOrden(arbol.Raiz())
    # arbol.Nivel(arbol.Raiz(),"3")
    #print(arbol.Altura(arbol.Raiz()))
    # arbol.Hijo(arbol.Raiz(),)