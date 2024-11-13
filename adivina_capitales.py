import random

def cargar_paises_y_capitales(archivo):
    paises_y_capitales = {}
    with open(archivo, 'r', encoding='utf-8') as file:
        for linea in file:
            pais, capital = linea.strip().split(',')
            paises_y_capitales[pais] = capital
    return paises_y_capitales

def juego_adivinar_capital(paises_y_capitales):
    puntaje = 0  
    
    while True:
        pais, capital_correcta = random.choice(list(paises_y_capitales.items()))
        
        print("¿Cuál es la capital de", pais, "?")
        respuesta = input("Tu respuesta: ")
        
        if respuesta.strip().lower() == capital_correcta.lower():
            print("¡Correcto! 🎉 Ganaste un punto.")
            puntaje += 1
        else:
            print("Incorrecto. La capital de ", pais, "es", capital_correcta)
        
        print("Puntaje actual: ", puntaje)
        
        if puntaje == 10:
            print("¡Felicidades! Has alcanzado 10 puntos y ganado el juego. 🎉")
            break
        
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            print("Puntaje final: ", puntaje)
            break

paises_y_capitales = cargar_paises_y_capitales("C:/Users/usuario/OneDrive/Escritorio/uni/python/TPI/paises_y_capitales.txt")
juego_adivinar_capital(paises_y_capitales)
