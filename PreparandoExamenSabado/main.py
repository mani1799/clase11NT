from Escuderia import Escuderia

escuderias=[]
contador=1
numeroEscuderias= int(input("Digite el numero de escuderias: "))
while numeroEscuderias < numeroEscuderias:
    escuderia=Escuderia()
    escuderia.nombre=input("digite el nombre de la escuderia")
    escuderia.__casaMotor=input("digite el nombre de la casa motor")
    escuderia.__pilotoPricipal.nombre=input("digite el nombre del piloto principal")
    escuderia.__pilotoPricipal.salarioAnual=input("digite el salario del piloto")
    escuderia.__pilotoPricipal.fechaNacimiento=input("digite la fecha de nacimiento del piloto principal")
    escuderia.__pilotoPricipal.Pais=input("digite el pais del piloto principal")
    escuderia.__piloto2.nombre=input("digite el nombre del piloto 2")
   
    escuderias.append(escuderia)
    contador=contador+1

