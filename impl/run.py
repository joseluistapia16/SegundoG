from  dominio.entidades import *
from menus.menuG import *
class Main:

    def __init__(self):
        self.men = MenuG()
        self.lista = []

    def start(self):
       tupla =["CREAR","CONSULTAR","ACTUALIZAR",
               "ELIMINAR","LISTAR","SALIR"]
       op = self.men.getMenu(tupla)
       if op== 1:
            self.__registro()
            self.start()
       if op==5:
            self.__listar()
            self.start()

    def __registro(self):
        print("\n\nREGISTRO DE PROVEEDORES")
        cedula = input("Cedula : ")
        nombre = input("Nombre :")
        direccion = input("Direccion:")
        codigo = input("Codigo:")
        obj = Proveedor(cedula,nombre,direccion,codigo)
        self.lista.append(obj)
        input("<Enter> para continuar...")

    def __listar(self):
        print("\n\nLISTA DE PROVEEDORES")
        for i in range(len(self.lista)):
            print(self.lista[i].getData())

        input("<Enter> para continuar...")

