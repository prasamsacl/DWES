# Adivinanza en Python
# Pregunta al usuario una adivinanza
print("Adivinanza:")

# Imprime por consola.
print("Tengo hojas, pero no soy un libro. Vivo en el jardín, pero no soy una flor. ¿Qué soy?")

# Imprime las opciones para que el usuario pueda elegir la respuesta correcta.
print("a) Un pájaro")
print("b) Un árbol")
print("c) Una flor")

# Obtener la respuesta del usuario
#  `input` permite al usuario introducir datos desde la consola y devuelve lo que se ingresa como una cadena.
respuesta = input("Elige una opción:")

# Verifica si la respuesta es correcta
if respuesta == "b":
    
    print("¡Correcto! La respuesta es un árbol.")
else:
    print("Respuesta incorrecta. La respuesta correcta es 'b) Un árbola'.")
