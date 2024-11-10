
import random

numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_intentos_max = 5
adivinado = False

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado:
    if not cant_intentos < cant_intentos_max: # Negacion
        print("¡Game over! No has podido adivinar dentro de los 5 intentos")
        break

    entrada = input("Introduce un número del 1 al 99: ") # TODO: convertir a numero
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número secreto es mayor a",numero)
    else:
        print("El número secreto es menor a:",numero)

    cant_intentos += 1

