# Realizar un Menú de Opciones y realizar una función para cada opción
#INICIO
print ("******** MENÚ *********")

# ENTRADA DE DATOS
# # Mostrar una lista de 3 servicios de pasaje con sus estrellas de calificación
print ("Califica la calidad del servicio de 1 a 5:")

Servicio_Pasaje = [
{
    "Servicio": "Metrobús",
    "Calificación": "🌟🌟🌟"
},
{
    "Servicio": "Metro",
    "Calificación": "🌟🌟"
},
{
    "Servicio": "Cablebús",
    "Calificación": "🌟🌟🌟🌟🌟"
},
]

# PROCESO /CALCULOS Y OPERACIONES/
Servicios = ["Metrobús", "Metro", "Cablebús"]

# EJECUCION Y PRUEBA
print ("Servicios de transporte:", Servicio_Pasaje)


# ENTRADA DE DATOS
# # Calcular la nómina de un empleado en ENERO del 2024
print ("Calcula la nómina mensual de un empleado en el mes de Mayo con un sueldo diario de $250")

PagoDiario = int(input("Ingresa el monto diario de lo que gana el empleado durante el mes de Mayo:"))

PagoMensual = PagoDiario * 31
IVAtrasladado= PagoMensual * (16 / 100)
Subtotal = PagoMensual + IVAtrasladado
IVAretenido = 2/3 * IVAtrasladado
ISRretenido = PagoMensual * (18 / 100)

# PROCESO /CÁLCULOS Y OPERACIONES/
PagoNeto = Subtotal - IVAretenido - ISRretenido
Pago = PagoNeto + (PagoDiario * 15)

Sueldo_Neto = [
{"Sueldo": print("Total:", Pago)
},
]

# EJECUCIÓN DE PROGRAMA
print("Pago Neto mensual del empleado:", Pago)


# c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error
# d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos