from procesos.data import *


class MenuG:

    def __init__(self):
        self.inpt = Data()
    def getMenu(self,tupla):
        for i in range(len(tupla)):
            print(str(i+1)+".- "+tupla[i]+".")
        op =0
        while op<=0 or op>len(tupla):
            op = self.inpt.inputInt("Ingrese una opcion[1.."+str(len(tupla))+"]:")
        return op

