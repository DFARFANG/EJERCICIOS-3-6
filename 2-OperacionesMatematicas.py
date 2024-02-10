#OPERACIONES MATEMÁTICAS

#Importar bibliotecas o lbrerías
import math

#ENTRADA DE DATOS
# #Declarar, crear o instancias variables o constantes
número_1 = int (input("ingresa un número: ")) #Casteo.- Es la conversión de un tipo de dato a otro.
número_2 = float (input("Ingresa otro número: "))

#PROCESOS (CÁLCULOS Y OPERACIONES MATEMÁTICAS Y LÓGICAS)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1	/ número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2) #Función Parámetros o Argumentos
cuadrado = número_1 ** 2
cubo = número_2 ** 3

raíz_cuadrada_1 = math.sqrt(número_1)
raíz_cuadrada_2 = pow(número_2, 1/2)
raíz_cúbica = pow(número_1, 1/3)

modulo_residuo = número_1 % número_2

#SALIDA DE DATOS
print("La suma es =", suma)
print("La resta es =", resta)
print("La multiplicación es =", multiplicación)
print("La división es =", división)
print("La potencia 1 es =", round(potencia_1, 2))
print("La potencia 2 es =", round(potencia_2, 2))
print("La raíz cuadrada 1 es =", (raíz_cuadrada_1, 2))
print("La raíz cuadrada 2 es =", (raíz_cuadrada_2, 2))
print("El modulo o residuo es =", modulo_residuo)