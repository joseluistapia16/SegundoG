from dominio.entidades import *
class Data:
    def getRepeat(self,lista,valor):
        res = False
        for i in range(len(lista)):
            if valor == lista[i]:
                res= True
                break
        return res

    def inputInt(self,msg):
        num=-1
        while num < 1:
            try:
                num = int(input(msg))
            except:
                print("Valor invalido!")
                num = -1
        return num

    def getProveedor(self,cedula,lista):
        obj = None
        for i in range(len(lista)):
            if cedula == lista[i].getCedula():
                obj = lista[i]
                break
        return obj

    def getPosProv(self,id,lista):
        pos = -1
        for i in range(len(lista)):
            if id == lista[i].getCedula():
                pos = i
                break
        return pos

