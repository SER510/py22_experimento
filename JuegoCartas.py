

from Deck import Baraja

class Jugador(object):
    def __init__(self, nombre='noname') -> None:
        self.mano = []
        self.nombre = nombre

        self.saludar()
    
    def coger_de_Baraja(self, Mazo, n):
        # self.mano = Mazo.quitar_carta()
        self.mano.append(Mazo.quitar_carta())

    def saludar(self):
        print('hola')


class Gamer(Jugador):
    def __init__(self, nombre) -> None:
        # self.nombre = nombre

        super().__init__(nombre)      # ejecutamos la funcion del mismo nombre de la clase "parent"
        

    def saludar(self):
        print('hola soy ', self.nombre)

class Juego(object):
    pass


class Partida(object):
    def __init__(self, lista_de_jugadores, baraja) -> None:
        
        self.jugadores = lista_de_jugadores
        self.baraja = baraja
        # self.cartas = baraja.cartas     # esto es lo que llamamos composicion
    
    def evaluar(self):
        pass

    def ronda(self):
        pass




gorka   = Jugador()
jorge   = Jugador('Jorge')
antonio = Gamer('Antonio')
print(antonio.mano)

# print(antonio.nombre)
# print(gorka.nombre)

print(Gamer.__mro__)
print(Juego.__mro__)

baraja1 = Baraja("española")

partida1 = Partida( [gorka, jorge], baraja1 )


