# NÓMINA DEL MES DE JUNIO

# INICIO
# ENTRADA DE DATOS /
PagoDiario = int(input("Ingresa el monto diario de lo que gana el empleado durante el mes de Mayo:"))

PagoMensual = PagoDiario * 31
IVAtrasladado= PagoMensual * (16 / 100)
Subtotal = PagoMensual + IVAtrasladado
IVAretenido = 2/3 * IVAtrasladado
ISRretenido = PagoMensual * (18 / 100)

# PROCESO /CÁLCULOS Y OPERACIONES/
PagoNeto = Subtotal - IVAretenido - ISRretenido
Pago = PagoNeto + (PagoDiario * 15)

# EJECUCIÓN DE PROGRAMA
print("El resultado del pago Neto mensual del empleado es:", Pago)