__author__ = "Juan Camilo López Díaz"
__version__ = "1.0.0"
__license__ = "GPL"
__email__ = "juanca110720@gmail.com"

from JuegoAhorcado import JuegoAhorcado, Estado
from Letra import Letra

def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida del juego."""
    print("=" * 50)
    print("🎮 BIENVENIDO AL JUEGO DEL AHORCADO 🎮")
    print("=" * 50)
    print("Adivina la palabra letra por letra.")
    print("Tienes 6 intentos antes de ser ahorcado.")
    print("¡Buena suerte!")
    print("=" * 50)

def mostrar_ahorcado(intentos_restantes):
    """Muestra el dibujo del ahorcado según los intentos restantes."""
    dibujos = [
        # 0 intentos - ahorcado completo 
        """
   +---+
   |   |
   O   |
  /|\  |
  /⌡\  |
       |
=========
        """,
        # 1 intento
        """
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
        """,
        # 2 intentos
        """
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
        """,
        # 3 intentos
        """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
        """,
        # 4 intentos
        """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
        """,
        # 5 intentos
        """
   +---+
   |   |
   O   |
       |
       |
       |
=========
        """,
        # 6 intentos - solo la horca
        """
   +---+
   |   |
       |
       |
       |
       |
=========
        """
    ]
    print(dibujos[intentos_restantes])

def mostrar_estado_juego(juego):
    """Muestra el estado actual del juego."""
    print("\n" + "=" * 30)
    
    # Mostrar la palabra con las letras adivinadas
    ocurrencias = juego.dar_ocurrencias()
    palabra_mostrar = " ".join(ocurrencias)
    print(f"Palabra: {palabra_mostrar}")
    
    # Mostrar intentos restantes
    intentos = juego.dar_intentos_disponibles()
    print(f"Intentos restantes: {intentos}")
    
    # Mostrar el ahorcado
    mostrar_ahorcado(intentos)
    
    # Mostrar letras ya jugadas
    jugadas = juego.dar_jugadas()
    if jugadas:
        letras_jugadas = [letra.dar_letra() for letra in jugadas]
        print(f"Letras jugadas: {', '.join(letras_jugadas)}")
    
    print("=" * 30)

def obtener_letra():
    """Solicita al usuario que ingrese una letra válida."""
    while True:
        entrada = input("\nIngresa una letra: ").strip().lower()
        
        if len(entrada) != 1:
            print("❌ Por favor, ingresa solo una letra.")
            continue
        
        if not entrada.isalpha():
            print("❌ Por favor, ingresa solo letras.")
            continue
        
        return Letra(entrada)

def jugar_partida():
    """Ejecuta una partida completa del juego."""
    juego = JuegoAhorcado()
    juego.iniciar_juego()
    
    print(f"\n🎯 Nueva partida iniciada!")
    print(f"La palabra tiene {len(juego.dar_palabra_actual().dar_letras())} letras.")
    
    while juego.dar_estado() == Estado.JUGANDO:
        mostrar_estado_juego(juego)
        
        letra = obtener_letra()
        
        # Verificar si la letra ya fue utilizada
        if juego.letra_utilizada(letra):
            print(f"⚠️ Ya has jugado la letra '{letra.dar_letra()}'.")
            continue
        
        # Jugar la letra
        resultado = juego.jugar_letra(letra)
        
        if resultado:
            print(f"✅ ¡Bien! La letra '{letra.dar_letra()}' está en la palabra.")
        else:
            print(f"❌ La letra '{letra.dar_letra()}' no está en la palabra.")
    
    # Mostrar resultado final
    mostrar_estado_juego(juego)
    
    if juego.dar_estado() == Estado.GANADOR:
        print("🎉 ¡FELICITACIONES! ¡Has ganado!")
        palabra_completa = "".join([letra.dar_letra() for letra in juego.dar_palabra_actual().dar_letras()])
        print(f"La palabra era: {palabra_completa.upper()}")
    elif juego.dar_estado() == Estado.AHORCADO:
        print("💀 ¡Has sido ahorcado! Mejor suerte la próxima vez.")
        palabra_completa = "".join([letra.dar_letra() for letra in juego.dar_palabra_actual().dar_letras()])
        print(f"La palabra era: {palabra_completa.upper()}")

def main():
    """Función principal del juego."""
    mostrar_bienvenida()
    
    while True:
        jugar_partida()
        
        print("\n" + "=" * 30)
        while True:
            respuesta = input("¿Quieres jugar otra partida? (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                break
            elif respuesta in ['n', 'no']:
                print("\n👋 ¡Gracias por jugar! ¡Hasta la próxima!")
                return
            else:
                print("❌ Por favor, responde 's' para sí o 'n' para no.")

if __name__ == "__main__":
    main()