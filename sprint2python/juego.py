import random

# Obtenemos la jugada del usuario
def obtener_jugada_usuario():
    while True:
        jugada = input("Elige tu jugada (piedra, papel o tijera): ").lower()
        if jugada in ["piedra", "papel", "tijera"]:
            return jugada
        else:
            print("Jugada no válida. Por favor, elige piedra, papel o tijera.")

# Obtenemos  la jugada aleatoria de la computadora
def obtener_jugada_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# Determinaremos el resultado de una jugada
def determinar_resultado(jugada_usuario, jugada_computadora):
    if jugada_usuario == jugada_computadora:
        return "Empate. Ambos eligisteis " + jugada_usuario + "."
    elif (
        (jugada_usuario == "piedra" and jugada_computadora == "tijera") or
        (jugada_usuario == "papel" and jugada_computadora == "piedra") or
        (jugada_usuario == "tijera" and jugada_computadora == "papel")
    ):
        return "Has ganado. " + jugada_usuario + " gana a " + jugada_computadora + "."
    else:
        return "Has perdido. " + jugada_computadora + " gana a " + jugada_usuario + "."

# Función principal del juego
def jugar_piedra_papel_tijera():
    puntuacion_usuario = 0
    puntuacion_computadora = 0
     # Realizaremos 5 rondas
    for _ in range(5): 
        jugada_usuario = obtener_jugada_usuario()
        jugada_computadora = obtener_jugada_computadora()

        resultado = determinar_resultado(jugada_usuario, jugada_computadora)
        print(resultado)

        if "Has ganado" in resultado:
            puntuacion_usuario += 1
        elif "Has perdido" in resultado:
            puntuacion_computadora += 1

    print("Resultado final después de 5 jugadas: Tú " + str(puntuacion_usuario) + " - " + str(puntuacion_computadora) + " Computadora")
    if puntuacion_usuario > puntuacion_computadora:
        print("¡Has ganado el juego!")
    elif puntuacion_usuario < puntuacion_computadora:
        print("Has perdido el juego.")
    else:
        print("El juego terminó en empate.")

if __name__ == "__main__":
    jugar_piedra_papel_tijera()
