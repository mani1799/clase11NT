from Piloto import Piloto

class Escuderia:
     def __init__(self):
        self.__nombre= None
        self.__casaMotor= None
        self.__pilotoPricipal= Piloto()
        self.__piloto2= Piloto()
        self.__costo=None


        @property

        def nombre(self):
             return self.__nombre
    
        @nombre.setter
        def nombre(self,dato):
            self.__nombre=dato

        @property

        def casaMotor(self):
             return self.__fechaNacimiento
        @casaMotor.setter
        def casaMotor(self,dato):
            self.__casaMotor=dato

        @property

        def pilotoPrincipal(self):
            return self.__pilotoPrincipal
        @pilotoPrincipal.setter
        def pilotoPrincipal(self,dato):
         self.__pilotoPrincipal

        @property

        def piloto2(self):
            return self.__piloto2
        @piloto2.setter
        def piloto2(self,dato):
         self.__piloto2

