import random

if __name__ == "__main__":
      # Inicializamos la puntuación del usuario en 0
    puntuacion = 0
    # Pondremos las 3 adivinanzas que teniamos de los ejercicios anteriores
    adivinanzas = {
        "Adivinanza 1": {
            "Pregunta": "Tengo hojas, pero no soy un libro. Vivo en el jardín, pero no soy una flor. ¿Qué soy?",
            "Opciones": {
                "a": "Un pájaro",
                "b": "Un árbol",
                "c": "Una flor",
            },
            "Respuesta": "b",
        },
        "Adivinanza 2": {
            "Pregunta": "Si me nombras, desaparezco. ¿Qué soy?",
            "Opciones": {
                "a": "Silencio",
                "b": "Oscuridad",
                "c": "Agua",
            },
            "Respuesta": "a",
        },
        "Adivinanza 3": {
            "Pregunta": "Tengo llaves pero no abro puertas. ¿Qué soy?",
            "Opciones": {
                "a": "Un perro",
                "b": "Un cofre",
                "c": "Un coche",
            },
            "Respuesta": "b",
        }
    }
    
     # Convierte las claves en una lista
    adivinanzas_disponibles = list(adivinanzas.keys())
     # Elije dos opciones al azar sin repetir
    adivinanzas_seleccionadas = random.sample(adivinanzas_disponibles, 2)
    # Iteramos a través de las adivinanzas seleccionadas
    for adivinanza in adivinanzas_seleccionadas:
        datos = adivinanzas[adivinanza]
        print(adivinanza + ":")
        print(datos["Pregunta"])
        for opcion, texto in datos["Opciones"].items():
            print(f"{opcion}) {texto}")

        respuesta = input("Elige una opción:")
        if respuesta == datos["Respuesta"]:
            print("¡Correcto! La respuesta es", datos["Opciones"][datos["Respuesta"]])
            puntuacion += 10
        else:
            print("Respuesta incorrecta. La respuesta correcta es", datos["Respuesta"], datos["Opciones"][datos["Respuesta"]])
            puntuacion -= 5
    # Imprime por pantalla el resultado total
    print("Tu puntuación final es:", puntuacion, "puntos.")
