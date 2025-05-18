print("1. Básico: imprime todos los números enteros del 0 al 100.\n")
for i in range(0, 101):
    if i % (51) == 0:
        print("\n")
    print(i, end=",")


print("2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500\n")
for i in range(2, 501):
    if i % 2 == 0:
        print(i, end=",")
    if i % (51) == 0:
        print("\n")

print(
    "3. Contando Vanilla Ice:\n",
    "a. imprime los números enteros del 1 al 100.",
    sep="   ",
)
print("   b. Si es divisible por 5 imprime “ice ice” en vez del número.")
print("   c. Si es divisible por 10, imprime “baby”")
for i in range(1, 101):
    print(i, end=",")
    if i % 10 == 0:
        print("\nbaby")
    elif i % 5 == 0:
        print("\nice ice")

print("4. Wow. Número gigante a la vista:")
print(
    "suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante)."
)
suma = 0
for i in range(0, 500001):
    if i % 2 == 0 and i != 0:
        suma += i
print(suma)

print(
    "5. Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3."
)
for i in range(2024, 1, -3):
    print(i, end=",")
    if i % (20) == 0:
        print("\n")

print("6. Contador dinámico:")
print("establece tres variables: numInicial, numFinal y multiplo.")
print(
    "Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo."
)
print(
    "Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas)."
)
inicial = int(input("Ingrese rango inicial :"))
final = int(input("Ingrese rango final :")) + 1
multiplo = int(input("Ingrese factor multiplo :"))
for i in range(inicial, final):
    if i % multiplo == 0:
        print(i, end=",")
