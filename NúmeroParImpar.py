# Pedir un Número Y Definir SI Es Par o Impar
# INICIO

# ENTRADA DE DATOS
NúmeroEntero = int (input("Ingresa un número entero="))

# PROCESO /DECLARAR VALORES Y CÁLCULOS/
NumNon = ((NúmeroEntero * 2) - 1)
residuo = NumNon % 4
if ((NumNon == residuo) and (NumNon == residuo)):
# SALIDA DE DATOS
    print ("El número es IMPAR")

NumPar = (NúmeroEntero / 2)
modulo_residuo = NumPar % 2 
if ((NumPar == modulo_residuo) and (NumPar == modulo_residuo)):
# SALIDA DE DATOS
    print ("El número es PAR")