from procesos.data import *


class MenuG:
    def getMenu(self,tupla):
        for i in range(len(tupla)):
            print(str(i+1)+".- "+tupla[i]+".")
        op =0
        while op<=0 or op>len(tupla):
            op = inputInt("Ingrese una opcion[1.."+str(len(tupla))+"]:")
        return op

