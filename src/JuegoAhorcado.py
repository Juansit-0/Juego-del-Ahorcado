import random
from enum import Enum
from typing import List
from Palabra import Palabra
from Letra import Letra


class Estado(Enum):
    NO_INICIADO = 1
    JUGANDO = 2
    GANADOR = 3
    AHORCADO = 4

class JuegoAhorcado:
    TOTAL_PALABRAS = 12
    MAX_INTENTOS = 6

    def __init__(self):
        self.diccionario: List[Palabra] = [
            Palabra("algoritmo"),
            Palabra("contenedora"),
            Palabra("avance"),
            Palabra("ciclo"),
            Palabra("indice"),
            Palabra("instrucciones"),
            Palabra("arreglo"),
            Palabra("vector"),
            Palabra("inicio"),
            Palabra("cuerpo"),
            Palabra("recorrido"),
            Palabra("patron"),
        ]
        
        # Atributos del estado del juego 
        self.palabra_actual: Palabra = None
        self.intentos_disponibles: int = self.MAX_INTENTOS
        self.jugadas: List[Letra] = []
        self.estado: Estado = Estado.NO_INICIADO

    def iniciar_juego(self):
        """Inicia un nuevo juego seleccionando una palabra aleatoria."""
        indice_aleatorio = random.randint(0, self.TOTAL_PALABRAS - 1)
        self.palabra_actual = self.diccionario[indice_aleatorio]
        self.intentos_disponibles = self.MAX_INTENTOS
        self.jugadas = []
        self.estado = Estado.JUGANDO

    def jugar_letra(self, letra: Letra) -> bool:
        """
        Juega una letra en el juego.
        :param letra: La letra a jugar.
        :return: True si la letra está en la palabra, False si no está.
        """
        if self.estado != Estado.JUGANDO:
            return False
        
        # Verificar si la letra ya fue utilizada
        if self.letra_utilizada(letra):
            return False
        
        # Agregar la letra a las jugadas
        self.jugadas.append(letra)
        
        # Verificar si la letra está en la palabra
        if self.palabra_actual.esta_letra(letra):
            # Verificar si se ganó el juego
            if self.palabra_actual.esta_completa(self.jugadas):
                self.estado = Estado.GANADOR
            return True
        else:
            # La letra no está en la palabra, reducir intentos
            self.intentos_disponibles -= 1
            
            # Verificar si se perdió el juego
            if self.intentos_disponibles == 0:
                self.estado = Estado.AHORCADO
            
            return False

    def dar_palabra_actual(self) -> Palabra:
        """Devuelve la palabra actual del juego."""
        return self.palabra_actual

    def dar_palabra(self, posicion: int) -> Palabra:
        """
        Devuelve la palabra en la posición especificada del diccionario.
        :param posicion: Posición de la palabra en el diccionario.
        :return: La palabra en la posición dada.
        """
        if 0 <= posicion < len(self.diccionario):
            return self.diccionario[posicion]
        return None

    def dar_intentos_disponibles(self) -> int:
        """Devuelve el número de intentos disponibles."""
        return self.intentos_disponibles

    def dar_jugadas(self) -> List[Letra]:
        """Devuelve la lista de letras jugadas."""
        return self.jugadas.copy()

    def dar_ocurrencias(self) -> List[str]:
        """
        Devuelve las ocurrencias de la palabra actual basadas en las jugadas.
        :return: Lista con las letras adivinadas o "_" para las no adivinadas.
        """
        if self.palabra_actual is None:
            return []
        return self.palabra_actual.dar_ocurrencias(self.jugadas)

    def dar_estado(self) -> Estado:
        """Devuelve el estado actual del juego."""
        return self.estado

    def letra_utilizada(self, letra: Letra) -> bool:
        """
        Verifica si una letra ya fue utilizada en el juego.
        :param letra: La letra a verificar.
        :return: True si la letra ya fue utilizada, False en caso contrario.
        """
        for jugada in self.jugadas:
            if jugada.es_igual(letra):
                return True
        return False

    def metodo1(self) -> str:
        return "Respuesta 1"

    def metodo2(self) -> str:
        return "Respuesta 2"