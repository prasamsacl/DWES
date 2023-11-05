#Definimos las calculadora.py como operaciones.py
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
    while True:
        # Solicitamos al usuario para que introduzca dos numeros
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        # Solicitamos al usuario que elija una operación
        print("Opciones de operaciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        opcion = input("Elija una operación: ")

        # Indicamos las operaciones que deseamos realizar dependiendo de la opción que hayamos escogido 
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
        
        # Preguntar al usuario si desea realizar otra operación
        #lower():  utiliza para convertir una cadena (string) en minúsculas, es decir, cambia todos los caracteres alfabéticos en la cadena a letras minúsculas. 
        otra_operacion = input("¿Deseas realizar otra operación? (s/n): ").lower()
        if otra_operacion != "s":
            break  # Salir del bucle si el usuario no desea seguir con las operaciones
