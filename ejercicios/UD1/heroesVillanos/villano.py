import numpy as np
import logging
from persona import Persona

class Villano(Persona):
    # Constructor de la clase Villano
    def __init__(self, name, last_name, birth_date):
        super().__init__(name, last_name, birth_date)
        
        # Traits específicos de villano con valores aleatorios (0-100)
        self.traits = {
            "Chagepeteador": np.random.randint(0, 101),  
            "EntregadorTardio": np.random.randint(0, 101),  
            "Ausencias": np.random.randint(0, 101),  
            "Hablador": np.random.randint(0, 101),  
        }
        
        # Calcular puntuación total basada en traits
        self._calculate_total_score()
        
        # Registrar creación del villano con traits en el log
        logging.info(f"Villano creado: {self.name} {self.last_name} - Traits: {self.traits}")

    # metodo para calcular la puntuación total del villano
    def _calculate_total_score(self):
        try:
            # Cálculo ponderado segun los pesos que me ha dado la gana ponerle
            base_score = 100
            
            # Factores de peso para cada trait negativo
            weights = {
                "Chagepeteador": 0.3,
                "EntregadorTardio": 0.25,
                "Ausencias": 0.25,
                "Hablador": 0.2
            }
            
            # Calcular penalización basada en traits ponderados
            penalty = sum(self.traits[trait] * weights[trait] for trait in self.traits)
            
            # Puntuación final (asegurándonos de que no baje de 0)
            self.points = max(0, base_score - penalty)
            
            logging.info(f"Puntuación total calculada para villano {self.name}: {self.points}")
            
        except Exception as e:
            logging.error(f"Error calculando puntuación para villano {self.name}: {e}")
            self.points = 0
    # Metodo para obtener el valor de un trait específico
    def get_trait_value(self, trait_name):
        return self.traits.get(trait_name)

    # Metodo para representar el villano como string
    def __str__(self):
        """Representación en string del villano"""
        traits_str = ", ".join([f"{trait}: {value}" for trait, value in self.traits.items()])
        return f"VILLANO - {super().__str__()} | Traits: {traits_str}"
