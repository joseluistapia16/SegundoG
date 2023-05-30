class Empleado:

    __codigo : str
    cedula : str
    nombre : str
    correo : str

    def __init__(self,p1,p2,p3,p4):
        Empleado.__codigo =p1
        Empleado.cedula = p2
        Empleado.nombre = p3
        Empleado.correo = p4

    def setCodigo(self,codigo):
        Empleado.__codigo= codigo

    def getCodigo(self):
        return Empleado.__codigo


    def getData(self):
        return Empleado.__codigo+" "+Empleado.cedula+" "+Empleado.nombre+" "+ Empleado.correo
"""
obj = Empleado("EMP001","095857","CARLOS LINO","jose@gmail.com")
obj.setCodigo("COD002")
obj.cedula="0986665"
print(obj.getData())
"""









class Metodos:

    def imprimir(self,nombre):
        return "Hola "+nombre

    def suma(self,x,y):
        return (x+y)
class Equipo_Futbol:

    def __init__(self,param1,param2,param3):
        self.nombre = param1
        self.__n_jugadores= param2
        self.estadio = param3

    def setN_jugadores(self,n_jugadores):
        self.__n_jugadores= n_jugadores
    def getN_jugadores(self):
        return self.__n_jugadores


    def getData(self):
        return self.nombre+" "+str(self.__n_jugadores)+" "+self.estadio

    def __getPrueba(self):
        return "Esto es una prueba"

class Persona:

    def __init__(self,cedula,nombre, direccion):
        self.__cedula = cedula
        self.nombre = nombre
        self.direccion = direccion

    def setCedula(self,cedula):
        self.__cedula = cedula

    def getCedula(self):
        return self.__cedula

    def getData(self):
        return self.__cedula+" "+self.nombre+" "+self.direccion

class Proveedor(Persona):

    def __init__(self,cedula,nombre,direccion,codigo):
        Persona.__init__(self,cedula,nombre, direccion)
        self.cod_prov = codigo

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+self.direccion+" "+self.cod_prov

class Cliente(Persona,Metodos):

    def __init__(self,cedula, nombre,direccion,codigo):
        Persona.__init__(self,cedula,nombre, direccion)
        self.cod_cli = codigo

    def imprimir(self,nombre):
        print("Hola")
        return "Estudiante "+nombre

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+self.direccion+" "+self.cod_cli

class Producto:

    def __init__(self,codigo, nombre, categoria):
        self.__codigo = codigo
        self.nombre = nombre
        self.categoria = categoria

    def setCodigo(self, codigo):
        self.__codigo= codigo

    def getCodigo(self):
        return self.__codigo



# Codigo de prueba


