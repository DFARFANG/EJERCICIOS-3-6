# FUNCIONES.- Son tareas específicas a ejecturar o realizar
# SINTAXIS:
'''
def Nombre_de_la_Función(parámetros o argumentos):
  instrucciones o procesos que va a realizar la función
  return valor        (Se dice que devuelve, retorna o regresa un valor)
'''

# Declarar o crear una Función
def Saludar(): # Verbos
  print("Hola Mundo")

def Sumar(a, b):  # La función obtiene o recibe 2 Parámetros o Argumentos
  suma = a + b
  return suma

def Restar(num1, num2):
  return num1 - num2

def Generar_contraseña(num_caracteres):
  if (num_caracteres <= 5):
    print("Contraseña creada de tantos caracteres")
  else:
    print("ERROR")

print("*********** MENÚ DE OPCIONES / MÓDULOS ***************")
print("❎ 1. Saludo")
print("😁 2. Suma")
print("😂 3. Resta")
print("4. Multiplicar")
print("5. Dividir")
opción = int(input("Ingresa una opción: "))

if (opción == 1):
  Saludar()   # Mandar a llamar o invocar una Función para ejecutarla
elif (opción == 2):
  print("La suma =", Sumar(10.5, 3)) # Mando a llamar la función y le paso o enviar los Parámetros o Argumentos
elif (opción == 3):
  print("La resta =", Restar(10, 5))
else:
  print("Opción no válida")
 6 changes: 6 additions & 0 deletions6  
OperacionesMatemáticas.py
@@ -1,12 +1,18 @@
# Operaciones Matemáticas

# PARADIGMA (Enfoque para realizar algo)
# ESTRUCTURADO: Secuencial, Selectivo/Decisivo e Iterativo
# FUNCIONAL/PROCEDIMIENTOS, DECLARATIVO (SQL), PROGRAMACIÓN ORIENTADA A OBJETOS, O A EVENTOS

# Importar bibliotecas o librerías de Funciones Matemáticas
import math

# ENTRADA DE DATOS 
# Declarar, crear o instancias variables o constantes
número_1 = float(input("Ingresa un número: ")) # CASTEO.- Conversión de un tipo de dato a otro tipo de dato
número_2 = float(input("Ingresa otro número: "))
# Declarar una CONSTANTE
PI = 3.1416

# PROCESOS (Cálculos y operaciones matemáticas y lógicas)
suma = número_1 + número_2