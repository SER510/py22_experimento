

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


baraja1 = Baraja("española")


partida1 = Partida( [gorka, jorge, antonio, lucas], baraja1 )
baraja1.mezclar()
jorge.coger_de_Baraja(baraja1,1)
print('carta de jorge', jorge.mano)


