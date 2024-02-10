# NIVEL DE AGUA EN METROS

# INICIO
print("NIVEL DE AGUA EN TINACO DE 6 METROS DE ALTURA")

# IMPORTAR BIBILIOTECA
import math

# ENTRADA DE DATOS /Pedir nivel de Agua/
Metros = float(input("Ingresa cantidad de agua en MTS:"))

# PROCESO /CALCULOS Y OPERACIONES/
    
    # # Condiciones
# /Menor de 0: FUGA EN CISTERNA DE AGUA/
if (Metros <= 0):
        print("FUGA DE AGUA")
# /Si se encuentra en Nivel 0: ENCENDER/
elif (Metros == 0):
        print("APAGAR BOMBA")
# /Entre 0 y 2 mts: ACELERAR BOMBA/
elif (Metros >= 0) and (Metros <= 2):
        print("SE REQUIERE ACELERAR BOMBA DE AGUA")
# /Entre 2 y 4 mts: BOMBA TRABAJANDO/
elif (Metros >= 2) and (Metros <=4):
        print("BOMBA TRABAJANDO ADECUADAMENTE")
# /Entre 4 y 6 mts: DESACELERAR BOMBA/
elif (Metros >= 4) and (Metros <=6):
        print("SE REQUIERE DESACELERAR BOMBA DE AGUA")
# /Si se encuentra en Nivel 6: APAGAR/
elif (Metros == 6):
        print("APAGAR BOMBA")
# /Si llega a más de 6 mts: DESBORDE/
else :
    print("🚨DESBORDAMIENTO DE AGUA EN CISTERNA🚨")

# SALIDA Y EJECUCION
## Se imprimen los resultados de las condiciones
# FIN DE PRUEBA 