## Tarea 1:

def eje1():
    semaforo = input("Semáforo?: ")
    if semaforo == "Verde":
        print("Cruzar la calle")
    else:
        print("Esperar")


def eje2():
    compra = int(input("Cuanto es la compra?: "))
    if compra > 100:
        descuento = compra*0.9
        precio = compra - descuento
    else:
        precio = compra
    print(precio)


def eje3():
    year = int(input("Que año es?: "))
    if year <= 2055:
        print(f"Informes del Año {year}")



def eje4():
    mi_lista = ["Jose", "Andreu", "Berk", "Cris"]
    for nombre in mi_lista:
        print(nombre)


def eje5(n):
    #Fibonacci:
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


def eje6():
    for num in range(1, 20):
        if num % 2 != 0:
            print(num)


def eje7():
    num_list = [1, 6, -4, -19, 57, -98]
    for neg in num_list:
        if neg < 0:
            print(neg)


def eje8():
    peso = float(input("Peso(en kg): "))
    estatura = float(input("Estatura(en metros): "))

    imc = peso / (estatura **2)

    print("Tu índice de masa corporal (IMC) es:", imc)


def eje9():

    # Solicitar la cantidad a invertir, el interés anual y el número de años
    cantidad_invertida = float(input("Ingresa la cantidad a invertir: "))
    tasa_interes_anual = float(input("Ingresa la tasa de interés anual (en porcentaje): "))
    years = int(input("Ingresa el número de años de la inversión: "))

    # Calcular el capital obtenido
    tasa_interes_decimal = tasa_interes_anual / 100  # Convertir el interés a decimal
    capital_obtenido = cantidad_invertida * (1 + tasa_interes_decimal) ** years

    # Redondear el capital obtenido a dos decimales
    capital_obtenido = round(capital_obtenido, 2)

    # Mostrar el capital obtenido
    print("El capital obtenido después de", years, "años es:", capital_obtenido)

def eje10():
    import random

    # Generar un número aleatorio entre 1 y 100 (puedes ajustar el rango según tus preferencias)
    numero_secreto = random.randint(1, 100)

    intentos = 0

    print("Adivina un numero entre 0-100!")

    while True:
        intentos += 1

        intento = int(input("Intento #" + str(intentos) + "->" + " Ingeresa un numero(0-100): "))

        if intento == numero_secreto:
            print("¡Felicidades! Adivinaste el número secreto", numero_secreto, "en", intentos, "intentos.")
            break
        elif intento < numero_secreto:
            print("El número secreto es mayor! Intenta de nuevo!")
        else:
            print("El número secreto es menor! Intenta de nuevo!")


def eje11(): #Ejercicio 12
    def intermedio(a, b):
        return (a + b) / 2

    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))

    resultado = intermedio(a, b)

    print(f"Intermedio de los numeros {a} y {b} es: {resultado}")

def eje12(): #Ejercicio 12+1
    def separar(lista):
        pares = []
        impares = []

        for num in lista:
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)

        return pares, impares


    lista = []

    for n in range(5):
        queda = 5
        num_lista = int(input(f"Crea una lista de 5! Quedan {queda-n} elementos: "))
        lista.append(num_lista)
        print(f"My list:  {lista}")
        print("-----")

    pares, impares = separar(lista)
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")


def eje13(): #Ejercicio 14

    a = int(input("Dame un numero que de quieres contar regresiva: "))

    def cuenta_atras(num):
        while num > 0:
            num -= 1
            print(num)

    cuenta_atras(a)


def eje14(): #Ejercicio 15
    def menorque(a, b):
        if a == b:
            print("Son iguales!")
        elif a < b:
            print(f"El numero menor es: {a}")
        else:
            print(f" El numero menor es: {b}")

    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))

    menorque(num1, num2)


def eje15(): # Ejercicio 16
    print("Dame 3 numeros! ")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    num3 = int(input("Numero 3: "))

    promedio = (num1 + num2 + num3) / 3

    print(f"Promedio de los 3 numeros: {promedio}")


def eje16(): #Ejercicio 17
    frase = input("Ingresa una frase!: ")
    char = input("una letra que quieres reempelazar con '-': ")

    frase_modificada = "".join("-" if c == char else c for c in frase)

    print(f"Frase modificada: {frase_modificada}")


def eje17(): #Ejercicio 18
    def sumatorioNumeros(a):

        # Inicializa una variable para llevar la suma de los dígitos
        total = 0

        # Itera sobre los dígitos y suma cada uno de ellos
        for d in str(a):
            total += int(d)

        return total

    numero = int(input("Numero: "))
    resultado = sumatorioNumeros(numero)
    print(f"Suma de los digitos {numero}: {resultado}")


def eje18(): #Ejercicio 19

    import numpy as np

    A = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
    B = np.array(([9, 8, 7], [6, 5, 4], [3, 2, 1]))

    resultado = np.dot(A, B)

    print(resultado)


if __name__ == '__main__':
    #eje1()
    #eje2()
    #eje3()
    #eje4()
    #print(eje5(8))
    #eje6()
    #eje7()
    #eje8()
    #eje9()
    #eje10()
    #eje11()
    #eje12()
    #eje13()
    #eje14()
    #eje15()
    #eje16()
    #eje17()
    eje18()
