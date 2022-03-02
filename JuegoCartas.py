

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
baraja1.mezclar()

partida1 = Partida( [gorka, jorge, antonio, lucas], baraja1 )

i = 0 #Ahora no sé hacerlo de otra forma y lo pongo así
for i in [1, 2, 3]:
    gorka.coger_de_Baraja(baraja1,1)
    jorge.coger_de_Baraja(baraja1,1)
    antonio.coger_de_Baraja(baraja1,1)
    lucas.coger_de_Baraja(baraja1,1)
    i = 1+i
    #Fin del bucle
    
print('Cartas de gorka', gorka.mano)
print('Cartas de jorge', jorge.mano)
print('Cartas de jorge', antonio.mano)
print('Cartas de jorge', lucas.mano)


