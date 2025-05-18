import json

# Cargar el contenido del archivo en la variable ventas
with open("/home/whernandez/sqlcmd/precurso-skillnest/datos/datos_de_carga.txt", "r", encoding="utf-8") as archivo:
    ventas = json.load(archivo)

# Mostrar las primeras ventas para verificar la carga
#print(ventas[:5])  # Muestra las primeras 5 entradas
def obtener_cantidad(item):
    return item["total_cantidad"]

def leer_diccionario(lista_ventas):
    #lista_ventas es mi db, y con la siguiente estructura leo sus registros
    total_cantidad=0
    ingresos_totales = 0
    ventas_por_producto =[]
    diccionario_temp = {}
    precios_por_producto = {}
    ingresos_por_dia = {}
    for registros in lista_ventas:
        #print(registros["fecha"],registros["producto"],registros["cantidad"],registros["precio"])
        fecha=registros["fecha"]
        producto=registros["producto"]
        cantidad=registros["cantidad"]
        precio=registros["precio"]
        total_venta=cantidad*precio
        total_cantidad += cantidad
        ingresos_totales += total_venta
       # Acumular por producto
        if producto in diccionario_temp:
            diccionario_temp[producto]["total_cantidad"] += cantidad
            diccionario_temp[producto]["total_venta"] += total_venta
        else:
            diccionario_temp[producto] = {"producto": producto,"total_cantidad": cantidad, "total_venta": total_venta}
        
        # Acumular en precios_por_producto 
        if producto in precios_por_producto:
            precios_por_producto[producto] = (
                precios_por_producto[producto][0] + total_venta,  # Suma de precios
                precios_por_producto[producto][1] + cantidad     # Suma de cantidades
            )
        else:
            precios_por_producto[producto] = (total_venta, cantidad)

        # Acumular ingresos por día 
        if fecha in ingresos_por_dia:
            ingresos_por_dia[fecha] += total_venta
        else:
            ingresos_por_dia[fecha] = total_venta

        ventas_por_producto = list(diccionario_temp.values())

    #print("Ventas por producto:", ventas_por_producto)
    print("Ingresos Totales =",ingresos_totales)
    print("Producto mas vendido :",max(ventas_por_producto, key=obtener_cantidad))
    print("\n","="*40,sep="")
    print("Precios promedio por producto:\n")
    print("PRODUCTO,","PRECIOS PROMEDIO,","CANTIDAD")
    for producto, (total_venta, total_cant) in precios_por_producto.items():
        promedio = total_venta / total_cant
        print(producto,",",round(promedio,2),",",total_cant)
    #Ventas por día
    print("\n","="*40,sep="")
    print("\nIngresos por día:")
    print("Fecha     ","PESOS CL")
    for fecha, total in ingresos_por_dia.items():
        print(fecha,round(total,2))

leer_diccionario(ventas)
