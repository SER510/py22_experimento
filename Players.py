class Jugador(object):
    def __init__(self, nombre='noname') -> None:
        self.mano = []
        self.nombre = nombre

        self.saludar()
    
    def coger_de_Baraja(self, Mazo, n):
        # self.mano = Mazo.quitar_carta()
        self.mano.append(Mazo.quitar_carta())

    def saludar(self):
        print('Hola')


class Gamer(Jugador):
    def __init__(self, nombre) -> None:
        # self.nombre = nombre

        super().__init__(nombre)      # ejecutamos la funcion del mismo nombre de la clase "parent"
        

    def saludar(self):
        print('Hola soy ', self.nombre)