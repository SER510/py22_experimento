from pickle import APPEND
from random import shuffle
from socket import NI_NUMERICHOST

class Baraja(object):
    """_summary_
        Genera una baraja nueva.
        Se ejecuta Baraja('europea')...
        daria de resultado...

    Args:
        object (_type_): _description_
    """
    malapraxis=1 #variable global de clase suele ser mala idea

    def __init__(self, tipoooo):
        """_summary_

        Args:
            tipoooo (str): _description_
        """
        cartas_local = []
<<<<<<< Updated upstream
        self.cartas = [1, 2, 3, 4, 5]   # lista
=======
        self.turno = 0
        self.numeros = [1, 2]   # lista
        self.numeros.extend(range(3,10))  # Extendemos la lista a 10 cartas por palo
        self.palos = ["corazon", "pica", "diamante", "trebol"]  # Creamos los palos de las cartas
>>>>>>> Stashed changes
        self.tipo = tipoooo             # tipo de baraja (española, francesa,...)
        self.cartas = []
        for n in self.numeros:
            for p in self.palos:
                carta = "{} de {}".format(n,p)
                self.cartas.append(carta) 

    def mezclar(self):
        shuffle(self.cartas)    # mezclamos el orden de las cartas
    
    def quitar_carta(self):
        return self.cartas.pop()