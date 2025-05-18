"""
Autor : William Hernandez
Fecha : 2025.05.17
RUT: 22.120.689-4

Funciones básicas 2 (Práctica)
Objetivos

Practicar la creación de funciones en Python
Familiarizarte el uso de listas
Acostumbrarte a la devolución de una expresión/valor en las funciones
"""
#1. Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos,
#   desde el 0 hasta el número proporcionado como entrada.
#Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]

def multiplica_por_2(Numero):
    lista_resultante=[]
    for i in range(0,Numero+1):
        lista_resultante.append(i*2)
    return lista_resultante

#2. Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
#Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
def suma_y_resta(lista1):
    # Se que recibire 2 numeros asi que 
    print(lista1[0]+lista1[1])
    return lista1[0]-lista1[1]

#3. Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
    #Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
def sumatoria_menos_longitud(lista2):
    suma = 0
    for i in lista2:
        suma += i
    return suma - len(lista2)

#4. Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número.
#   Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
#   Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
#   Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]
def valores_multiplicados_segundo(lista3):
    long_lista=len(lista3)
    if long_lista < 2:
        return "[]"
    else:
        segundo=lista3[1]
        return [valores_lista*segundo for valores_lista in lista3]

#5. Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud.
#   La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
#   Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
#   Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]    
def valor_multiplicado_longitud(valor,longitud):
    lista4=[]
    for i in range(0,longitud):
        lista4.append(valor*longitud)
    return lista4

#*******************************************************************
#Solución 1
print("\nEjercicio 1 : Multiplica por 2\n","***********\n",sep="")
print(multiplica_por_2(5))

#Solución 2
print("\nEjercicio 2 : Suma y resta\n","***********\n",sep="")
print(suma_y_resta([5,4]))

#Solución 3
print("\nEjercicio 3 : Sumatoria menos longitud\n","***********\n",sep="")
print(sumatoria_menos_longitud([1, 2, 3, 4]))

#Solucion 4.1
print("\nEjercicio 4.1 : Sumatoria menos longitud\n","***********\n",sep="")
print(valores_multiplicados_segundo([1, 3, 5, 7]))
print("\nEjercicio 4.2 : Sumatoria menos longitud\n","***********\n",sep="")
#Solucion 4.2
print(valores_multiplicados_segundo([1]))

#Solucion 5.1
print("\nEjercicio 5.1 : Sumatoria menos longitud\n","***********\n",sep="")
print(valor_multiplicado_longitud(5, 2))
print("\nEjercicio 5.2 : Sumatoria menos longitud\n","***********\n",sep="")
#Solucion 5.2
print(valor_multiplicado_longitud(7, 5))
