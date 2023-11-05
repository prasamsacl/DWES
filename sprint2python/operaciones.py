# operaciones.py

def suma(a, b):
    """ Suma."""
    return a + b

def resta(a, b):
    """ Resta."""
    return a - b

def multiplicacion(a, b):
    """ Multiplicación."""
    return a * b

def division(a, b):
    """ División con control de división por 0."""
    if b == 0:
        return "Error: División por 0"
    else:
        return a // b  # División entera (//) para obtener un resultado entero

if __name__ == "__main__":
    # Solicitar los dos números al usuario
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    # Solicitar al usuario que elija una operación
    print("Opciones de operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elija una operación: ")

    # Indicamos las operaciones que deseamos realizar dependiendo de la opcion que hayamos escogido 
    if opcion == "1":
        resultado = suma(a, b)
        print(a, "+", b, "=", resultado)
    elif opcion == "2":
        resultado = resta(a, b)
        print(a, "-", b, "=", resultado)
    elif opcion == "3":
        resultado = multiplicacion(a, b)
        print(a, "*", b, "=", resultado)
    elif opcion == "4":
        resultado = division(a, b)
        if isinstance(resultado, int):
            print(a, "/", b, "=", resultado)
        else:
            print(resultado)
    else:
        print("Opción no válida. Por favor, elija una opción válida.")