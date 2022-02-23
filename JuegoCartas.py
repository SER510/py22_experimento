

from Deck import Baraja

from Players import Jugador
from Players import Gamer

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
<<<<<<< Updated upstream
lucas = Gamer('Lucas')
=======
edgar   = Gamer('Edgar')
>>>>>>> Stashed changes
print(antonio.mano)

# print(antonio.nombre)
# print(gorka.nombre)

print(Gamer.__mro__)
print(Juego.__mro__)

baraja1 = Baraja("española")

partida1 = Partida( [gorka, jorge, antonio, lucas], baraja1 )


