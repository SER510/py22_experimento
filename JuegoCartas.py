

from Deck import Baraja

from Players import Jugador
from Players import Gamer
from GameType import Partida

class Juego(object):
    pass







gorka   = Jugador()
jorge   = Jugador('Jorge')
antonio = Gamer('Antonio')
lucas = Gamer('Lucas')
print(antonio.mano)

# print(antonio.nombre)
# print(gorka.nombre)

print(Gamer.__mro__)
print(Juego.__mro__)

baraja1 = Baraja("española")

partida1 = Partida( [gorka, jorge, antonio, lucas], baraja1 )


