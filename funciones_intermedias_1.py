"""
Autor : William Hernández
Fecha : 2025.05.17
RUT: 22.120.689-4
"""

#1. Actualizar valores en diccionarios y listas

# Solucion 1
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
def cambio_valor(lista_matriz):
    for x in range(len(lista_matriz)):
        for y in range(len(lista_matriz[x])):
            if lista_matriz[x][y] == 3:
                lista_matriz[x][y] = 6
                return lista_matriz



#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
def cambio_nombre(diccionario_cantantes,cantante_old,cantante_new):
    #se recibe una lista que contienen 2 elementos conteniendo diccionarios
    for cantante in diccionario_cantantes:
        if cantante["nombre"]== cantante_old:
            cantante["nombre"]=cantante_new
    return diccionario_cantantes

#En ciudades, cambia “Cancún” por “Monterrey”
def cambio_ciudad(diccionario_ciudad,ciudad_actual,ciudad_nueva):
    #Recorro cada país (clave) y su lista de ciudades:
    for paises in diccionario_ciudad:
       #Recorro cada ciudad por su índice:
       for i in range(len(diccionario_ciudad[paises])):
            if diccionario_ciudad[paises][i]==ciudad_actual:
                diccionario_ciudad[paises][i]=ciudad_nueva
    return diccionario_ciudad

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
def cambio_coordenada(lista_cordenadas,clave,valor):
    for posicion in lista_cordenadas:
        posicion[clave]=valor
    return lista_cordenadas

#**************************************************************************
#Solución 1.1
print("\nSolucion 1.1 : Cambio de valor en lista\n","***********\n",sep="")
print(cambio_valor(matriz))

#Solución 1.2
print("\nSolucion 1.2 : Cambio de valor en lista\n","***********\n",sep="")
buscar = "Ricky Martin"
actualizar = "Enrique Martin Morales"
print(cambio_nombre(cantantes,buscar,actualizar))

#Solución 1.3
print("\nSolucion 1.3 : Cambio de valor en lista\n","***********\n",sep="")
print(cambio_ciudad(ciudades,"Cancún","Monterrey"))

#Solución 1.4
print("\nSolucion 1.4 : Cambio de valor en lista\n","***********\n",sep="")
print(cambio_coordenada(coordenadas,"latitud",9.9355431))

#*******************************************************
#2. Iterar a través de una lista de diccionarios

#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.
#  Por ejemplo:

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

#Solución 2
print("\nSolucion 2 : Cambio de valor en lista\n","***********\n",sep="")

def iterarDiccionario(lista_cantantes):
    for cantantes in lista_cantantes:
        print("nombre",cantantes["nombre"],"país",cantantes["pais"],sep=" - ")

iterarDiccionario(cantantes)

#3. Obtener valores de una lista de diccionarios
#   Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios.
#   La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo,
#   iterarDiccionario2(“nombre”, cantantes) debe de imprimir:
#       Ricky Martin
#       Chayanne
#       José José
#       Juan Luis Guerra

#Solucion 3
def iterarDiccionario2(clave,lista):
    for cantantes in lista:
        print(cantantes[clave])

print("\nSolucion 3 : Obtener valores de una lista de diccionarios\n","***********\n",sep="")
for claves in ["nombre","pais"]:
    print("Lista por",claves,"\n",end="="*20)
    print("")
    iterarDiccionario2(claves, cantantes)
    print("")

#4. Iterar a través de un diccionario con valores de lista
#   Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas.
#   La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

#Solucion 4
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(clave):
    print("LISTA POR",clave.upper(),"\n")
    longitud_lista =len(costa_rica[clave])
    print("***",longitud_lista,clave.upper(),"***")
    for i in range(longitud_lista):
        #las listas las accedo por inice
        print(costa_rica[clave][i])

print("\nSolucion 4 : Iterar a través de un diccionario con valores de lista\n","***********\n",sep="")
for diccionario in ["ciudades","comidas"]:
    imprimirInformacion(diccionario)
    print("")