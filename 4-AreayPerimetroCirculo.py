#CÓDIGO PARA CALCULAR ÁREA X Y PERÍMETRO Y DE UN CÍRCULO

#IMPORTAR BIBILIOTECA
import math

# #ENTRADA DE DATOS
    #Valor de radio

radio = float (input("Ingrese LONGITUD de RADIO en CENTIMETROS:")) 
PI = 3.1416

#PROCESO
área = PI * (radio ** 2)
perímetro = PI * (radio *2)

#SALIDA Y EJECUCIÓN
print("El resultado de área es= ", round(área, 2))
print("y perímetro es= ", round(perímetro, 2))
