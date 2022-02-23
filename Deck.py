from random import shuffle

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
        self.cartas = [1, 2, 3, 4, 5]   # lista
        self.tipo = tipoooo             # tipo de baraja (española, francesa,...)

    def mezclar(self):
        shuffle(self.cartas)    # mezclamos el orden de las cartas
    
    def quitar_carta(self):
        return self.cartas.pop()