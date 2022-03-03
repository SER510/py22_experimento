

from Deck import Baraja

from Players import Jugador
from Players import Gamer
from GameType import Partida

import numpy as np

class Juego(object):
    pass    


print("Número de jugadores")
num_jugadores = int(input())
#print("Hay ", num_jugadores, " jugadores")

jugadores = np.empty(num_jugadores, dtype=object)

for i in range(num_jugadores):
    print("Nombre de jugador ", i+1)
    nombres = input()
    jugadores[i] = Gamer(nombres)


print("  ")


baraja1 = Baraja("francesa")
baraja1.mezclar()


partida1 = Partida( jugadores, baraja1)


print("  ")


print("Cartas que cogerá cada jugador")
num_cartas = int(input())
for i in range(num_cartas):
    for j in range(num_jugadores):
        jugadores[j].coger_de_Baraja(baraja1,1)



for n in range(num_jugadores):
    print('Cartas de Jugador', n+1, jugadores[n].mano)

########################################################
##### CÓDIGO QUE TENÍAMOS ANTES

# gorka   = Jugador()
# jorge   = Jugador('Jorge')
# antonio = Gamer('Antonio')
# lucas = Gamer('Lucas')

# baraja1 = Baraja("española")
# baraja1.mezclar()

# partida1 = Partida( [gorka, jorge, antonio, lucas], baraja1 )

# i = 0 #Ahora no sé hacerlo de otra forma y lo pongo así
# for i in [1, 2, 3]:
#     gorka.coger_de_Baraja(baraja1,1)
#     jorge.coger_de_Baraja(baraja1,1)
#     antonio.coger_de_Baraja(baraja1,1)
#     lucas.coger_de_Baraja(baraja1,1)
#     i = 1+i
#     #Fin del bucle

# print('Cartas de gorka', gorka.mano)
# print('Cartas de jorge', jorge.mano)
# print('Cartas de antonio', antonio.mano)
# print('Cartas de lucas', lucas.mano)



