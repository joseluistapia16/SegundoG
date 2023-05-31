from  dominio.entidades import *
from menus.menuG import *
from procesos.data import *
from archivos.archivo import *
class Main:

    def __init__(self):
        self.ruta = "C:/Users/Usuario/PycharmProjects/SegundoG/segundog.csv"
        self.men = MenuG()
        self.lista = []
        self.proc = Data()
        self.arch = Archivo()
        self.lista= self.arch.getProveedores(self.ruta)

    def start(self):
       tupla =["CREAR","CONSULTAR","ACTUALIZAR",
               "ELIMINAR","LISTAR","SALIR"]
       op = self.men.getMenu(tupla)
       if op== 1:
            self.__registro()
            self.start()
       if op==2:
            self.__consulta()
            self.start()
       if op==3:
           self.__actualizar()
           self.start()
       if op==4:
           self.__eliminar()
           self.start()
       if op==5:
            self.__listar()
            self.start()

    def __registro(self):
        print("\n\nREGISTRO DE PROVEEDORES")
        cedula = input("Cedula : ")
        self.lista= self.arch.getProveedores(self.ruta)
        pos = self.proc.getPosProv(cedula,self.lista)
        if pos==-1:
            nombre = input("Nombre :")
            direccion = input("Direccion:")
            codigo = input("Codigo:")
            obj = Proveedor(cedula,nombre,direccion,codigo)
            registro=obj.getCedula()+";"+obj.nombre+";"+obj.direccion+";"\
                     +obj.cod_prov+";\n"
            self.arch.create(self.ruta,registro,"a")
            print("Datos grabados!")
        else:
            print("Cedula ya existe!")
        input("<Enter> para continuar...")

    def __consulta(self):
        print("\t\tCONSULTA DE PROVEEDORES")
        id = input("Cedula:")
        self.lista=self.arch.getProveedores(self.ruta)
        obj = self.proc.getProveedor(id,self.lista)
        if obj!= None:
            print(obj.getFields())
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")

    def __actualizar(self):
        print("\t\tACTUALIZACION DE PROVEEDORES")
        id = input("Cedula:")
        self.lista= self.arch.getProveedores(self.ruta)
        pos = self.proc.getPosProv(id,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            nombre = input("Nombre :")
            direccion = input("Direccion:")
            codigo = input("Codigo:")
            self.lista[pos].nombre = nombre
            self.lista[pos].direccion= direccion
            self.lista[pos].cod_prov = codigo
            msg =""
            for i in range(len(self.lista)):
                msg = msg + self.lista[i].getCedula()+";"+self.lista[i].nombre\
                      +";"+self.lista[i].direccion+";"+self.lista[i].cod_prov+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Datos actualizados!")
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")

    def __eliminar(self):
        print("\t\tELIMINAR DATOS DE PROVEEDORES")
        id = input("Cedula:")
        self.lista= self.arch.getProveedores(self.ruta)
        pos = self.proc.getPosProv(id,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            self.lista.pop(pos)
            msg = ""
            for i in range(len(self.lista)):
                msg= msg+self.lista[i].getCedula()+";"+self.lista[i].nombre+\
                     ";"+self.lista[i].direccion+";"+self.lista[i].cod_prov+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Datos eliminados!")
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")



    def __listar(self):
        print("\n\nLISTA DE PROVEEDORES")
        self.lista= self.arch.getProveedores(self.ruta)
        for i in range(len(self.lista)):
            print(self.lista[i].getData())

        input("<Enter> para continuar...")

