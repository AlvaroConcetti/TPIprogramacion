import random
# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 10)

# Función para mostrar el estado del juego
def mostrar_tablero(jugadores, casillas):
    print("\nEstado actual del tablero:")
    for jugador in jugadores:
        print(jugador['nombre'] , " está en la casilla " , str(jugador['posicion']))
    print("Casillas totales: " , str(casillas))
    print()

# Función para realizar un turno
def turno(jugador, casillas):
    print("\nEs el turno de " , jugador['nombre'] , ".")
    input("Presiona Enter para lanzar el dado...")
    
    # Lanzar el dado
    dado = lanzar_dado()
    print(jugador['nombre'] , " lanzó el dado y sacó un " , str(dado) , ".")
    
    # Avanzar el jugador
    jugador['posicion'] += dado
    
    # Verificar si ha alcanzado o superado la casilla 63
    if jugador['posicion'] >= casillas:
        jugador['posicion'] = casillas
        print("¡" , jugador['nombre'] , " ha llegado a la última casilla y ha ganado!")
        return True
    
    print(jugador['nombre'] , " avanza a la casilla " , str(jugador['posicion']) , ".")
    return False

# Función principal del juego
def jugar():
    # Configuración inicial
    casillas = 100  # Última casilla
    jugadores = [
        {'nombre': 'Jugador 1', 'posicion': 0},
        {'nombre': 'Jugador 2', 'posicion': 0}
    ]
    
    # Bucle del juego
    while True:
        for jugador in jugadores:
            mostrar_tablero(jugadores, casillas)
            
            # Realizar el turno del jugador
            if turno(jugador, casillas):
                return  # Si algún jugador llega a la última casilla, termina el juego.

if __name__ == "__main__":
    print("¡Bienvenidos al Juego de la Oca !")
    jugar()
