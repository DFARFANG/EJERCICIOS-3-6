# ARREGLOS / LISTAS.- Variable que almacena una colección de datos de uno o distintos tipo de datos
# SINTAXIS:
'''
nombre_del_arreglo = [valor1, valor2, valor3, ...]
index                   0       1       2 ....  3
A los valores de la colección también se le llamas elemento
'''
# Formato JSON: Arreglos de Diccionarios
datos_personas = [
  {
    "Nombre": "Ivette",
    "Edad": 41
  },
  {
    "Nombre": "Daniel",
    "Edad": 30
  },
  {
    "Nombre": "Diego",
    "Edad": 40
  }
]

# Declarar o crear una Lista
números = [] # lista vacía

nombres = ["Ivette", "Daniel", "Diego"]
# índice:      0          1       2    index
edades = [20, 30, 40]

# OPERACIONES CON ARREGLOS / LISTAS
# Agregar o insertar un elemento al final de la lista
nombres.append("Eduardo")
edades.append(50)

# Eliminar un elemento de una lista
nombres.remove("Daniel")
edades.remove(30)

# Acceder y editar a un elemento de una lista
nombres[0] = "Juana Ivette"
edades[0] = 41

# Obtener la longitud de una lista o arreglo
print(len(nombres)) # lenght
print(len(edades))

# Ordenar una lista o arreglo
nombres.sort()              # ASCENDENTE Alfabética o Consecutivos
edades.sort(reverse=True)   # DESCENDENTE

print("NOMBRES:", nombres)
print("EDADES:", edades)