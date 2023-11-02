if __name__ == "__main__":
    # Inicializa la puntuación del usuario en 0
    puntuacion = 0

    #las 3 adivinanzas 
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

    # Itera a través de las adivinanzas
    for adivinanza, datos in adivinanzas.items():
        print(adivinanza + ":")
        print(datos["Pregunta"])
        for opcion, texto in datos["Opciones"].items():
            print(f"{opcion}) {texto}")

        respuesta = input("Elige una opción:")
        if respuesta == datos["Respuesta"]:
            print(f"¡Correcto! La respuesta es {datos['Opciones'][datos['Respuesta']]}")
            puntuacion += 10
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es '{datos['Respuesta']} {datos['Opciones'][datos['Respuesta']]}'")
            puntuacion -= 5

    # imprime por pantalla el resultado total
    print(f"Tu puntuación final es: {puntuacion} puntos.")
