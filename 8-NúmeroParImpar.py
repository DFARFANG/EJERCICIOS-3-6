# Pedir un Número Y Definir SI Es Par o Impar
# INICIO

#IMPORTAR LIBRERIA
import math
# ENTRADA DE DATOS
NúmeroEntero = int(input("Ingresa un número entero="))

# PROCESO /DECLARAR VALORES Y CÁLCULOS para IMPAR/
NumNon = (NúmeroEntero % 2)
if ((NumNon != 0) and (NumNon ==1)):
# SALIDA DE DATOS
    print ("El número es IMPAR")
    
# PROCESO /DECLARAR VALORES Y CÁLCULOS para PAR/
NumPar = (NúmeroEntero % 2)
modulo_residuo = NumPar / 2 
if ((NumPar == modulo_residuo) and (NumPar == modulo_residuo)):
# SALIDA DE DATOS
    print ("El número es PAR")