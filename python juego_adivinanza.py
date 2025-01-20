import random


def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza!")
    print("He elegido un número entre 1 y 100. ¡Tienes 7 intentos para adivinarlo!")

    # Configuración del juego
    numero_correcto = random.randint(1, 100)  # Número aleatorio entre 1 y 100
    intentos_restantes = 7  # Número máximo de intentos

    while intentos_restantes > 0:
        try:
            # Entrada del usuario
            adivinanza = int(input(f"Te quedan {intentos_restantes} intentos. Ingresa tu número: "))

            # Verificar si la adivinanza es correcta
            if adivinanza == numero_correcto:
                print("¡Felicidades! Has adivinado el número correctamente.")
                break
            elif adivinanza < numero_correcto:
                print("El número es mayor.")
            else:
                print("El número es menor.")

            # Reducir intentos
            intentos_restantes -= 1
        except ValueError:
            print("Por favor, ingresa un número válido.")  # Manejar errores de entrada

    # Fin del juego
    if intentos_restantes == 0:
        print(f"Lo siento, te has quedado sin intentos. El número correcto era {numero_correcto}.")
    print("Gracias por jugar. ¡Hasta la próxima!")


# Ejecutar el juego
if _name_ == "_main_":
    juego_adivinanza()