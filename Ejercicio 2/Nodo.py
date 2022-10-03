class Nodo:
    __elemento=None
    __sigD=None
    __sigI=None
    def __init__(self,elemento=None):
        self.__elemento=elemento
        self.__sigD=None
        self.__sigI=None
    def setSigD(self, siguiente):
        self.__sigD=siguiente
    def getSigD(self):
        return self.__sigD
    def setSigI(self, siguiente):
        self.__sigI=siguiente
    def getSigI(self):
        return self.__sigI
    def getElemento(self):
        return self.__elemento
    def setElemento(self,elemento):
        self.__elemento=elemento
    def __gt__(self,otro):
        retorna=False
        if self.getElemento() < otro.getElemento():
            retorna=True
        return retorna