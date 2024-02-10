# OBTENER VALORES PARA A, B Y C
# CALCULAR FÓRMULA GENERAL

#IMPORTAR BIBILIOTECA
import math

# DECLARAR ESTRUCTURA DE ECUACIÓN
print ("La ecuación se estructura de la siguiente manera: ax^2 + bx + c")
print ("Sutituir valores de A, B y C")

# Entrada de Datos A
A = int (input("Designar valor a A:")) 

# Entrada de Datos B
B = int (input("Designar valor a B:"))

# Entrada de Datos C
C = int (input("Designar valor a C:"))

#  Proceso /Calculos y Operaciones/
FormulaGeneral = B - pow(((B ** 2) - (4 * A) * C), 1/2) / 2 * A

# Salida y Ejecución
print ("El valor de X es =", round(FormulaGeneral, 1))

# Proceso /Designar valores en Ecuación Cuadrática/
EcuaciónCuadrática = ((A * FormulaGeneral) ** 2) + (B * FormulaGeneral) + C

# Salida de Datos
print ("El resultado de la Ecuación Cuadrática es=", round(EcuaciónCuadrática, 2))