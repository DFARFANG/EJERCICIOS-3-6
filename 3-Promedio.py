# CALCULAR PROMEDIO EN 3 CALIFICACIONES DE UNA PERSONA

#ENTRADA DE DATOS
    #Declarar constantes
número_1 = float (input("Ingresa calificación de materia 1 CON VALORES DECIMALES:")); #Valores decimales para aplicar la utilización de variable float
número_2 = float (input("Ingresa calificación de materia 2 CON VALORES DECIMALES:"));
número_3 = float (input("Ingresa calificación de materia 3 CON VALORES DECIMALES:"));

#PROCESO
suma = número_1 + número_2 + número_3
división = suma / 3
#SALIDA DE DATOS
print("El promedio de las 3 materias es= ", división);