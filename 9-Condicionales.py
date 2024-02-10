#Condicionales. Mayor o Menor de edad.

#ENTRADA DE DATOS
    #Declarar una variable
edad = int(input("Ingresa tu edad:"))

#PROCESOS
if (edad >= 18) and (edad <= 120):
    print("Mayor de edad")
elif (edad < 18) and (edad >= 0):
    print("Menor de edad")
elif (edad <= -1) or (edad >= 121):
    print("Error")

#FIN DE PRUEBA