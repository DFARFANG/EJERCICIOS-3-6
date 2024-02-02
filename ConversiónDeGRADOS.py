# CONVERSIÓN DE GRADOS
# INICIO
#Importar bibliotecas o lbrerías
import math

# Entrada de Datos
GradoCelsiusK = float (input("Ingresa cantidad en Grados Kelvin para convertir en C:"))
GradoFahrenK = float (input("Ingresa cantidad en Grados Kelvin para convertir en F:"))
GradoFahrenC = float (input("Ingresa cantidad en Grados Celcius para convertir en F:"))
GradoKelvinC = float (input("Ingresa cantidad en Grados Celcius para convertir en K:"))
GradoCelsiusF = float (input("Ingresa cantidad en Grados Fahrenheit para convertir en C:"))
GradoKelvinF = float (input("Ingresa cantidad en Grados Fahrenheit para convertir en K:"))

# Proceso /Calculos y Operaciones/
operación_1 = GradoCelsiusK - 273.15
operación_2 = (GradoFahrenK - 273.15) / 5 + 32
operación_3 = (9 * GradoFahrenC / 5) + 32
operación_4 = GradoKelvinC + 273.15
operación_5 = 5 * (GradoCelsiusF - 32) / 9
operación_6 = 5 * (GradoKelvinF - 32) / 9 + 273.15

# Salida y Ejecución
print ("Su resultado de Kelvin en Celcius es=", round(operación_1, 2))
print ("Su resultado de Kelvin en Fahrenheit es=", round(operación_2, 2))
print ("Su resultado de Celsius en Fahrenheit es=", round(operación_3, 2))
print ("Su resultado de Celsius en Kelvin es=", round(operación_4, 2))
print ("Su resultado de Fahrenheit en Celcius es=", round(operación_5, 2))
print ("Su resultado de Fahrenheit en Kelvin es=", round(operación_6, 2))

# Fin de Prueba