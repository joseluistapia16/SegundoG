from  dominio.entidades import *
class Main:

    def start(self):
        """
        obE = Equipo_Futbol("BSC",24,"BANCO PICHINCHA")
        print(obE.getData())
        obE.setN_jugadores(45)
        obE.nombre="EMELEC"
        print(obE.getData())

        obCl = Cliente("12345","Alex Quiroz","GARZOTA","CL001")
        print(obCl.getData())
        obCl.setCedula("0978654")
        obCl.nombre="TANIA MORALES"
        print(obCl.getData())
        print(obCl.imprimir("Torres"))
        """
        lista = []
        obCl1 = Cliente("12345", "Alex Quiroz", "GARZOTA", "CL001")
        obCl2 = Cliente("09876", "Maria Mora", "URDESA", "CL002")
        obCl3 = Cliente("65432", "Veronica Vera", "CENTRO", "CL003")
        obCl4 = Cliente("23456", "Carmen Parra", "CEIBOS", "CL004")
        obCl5 = Cliente("048947", "Diego Lopez", "CENTENARIO", "CL005")
        lista.append(obCl1)
        lista.append(obCl2)
        lista.append(obCl3)
        lista.append(obCl4)
        lista.append(obCl5)
        for i in range(len(lista)):
            print(lista[i].getData())