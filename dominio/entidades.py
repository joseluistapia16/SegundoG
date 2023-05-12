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

# Codigo de prueba
obE = Equipo_Futbol("BSC",24,"BANCO PICHINCHA")
print(obE.getData())
obE.setN_jugadores(45)
obE.nombre="EMELEC"
print(obE.getData())