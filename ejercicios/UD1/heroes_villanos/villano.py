import numpy as np
from persona import Persona

class Jugador(Persona):

    def __init__(self, name, last_name, birth_date):
        super().__init__(name, last_name, birth_date)
        self.traits = {
          "Chagepeteador": np.random.randint(0, 100),
          "EntregadorTardio": np.random.randint(0, 100),
          "Ausencias": np.random.randint(0, 100),
          "Hablador": np.random.randint(0, 100),
        }
        
