import numpy as np
import logging
from persona import Persona

class Heroe(Persona):
    
    # Constructor de la clase Héroe
    def __init__(self, name, last_name, birth_date):
        super().__init__(name, last_name, birth_date)
        
        # Traits específicos de héroe con valores aleatorios (0-100) Uso un diccionario porque necesito asociar nombre y valor
        self.traits = {
            "CodigoLimpio": np.random.randint(0, 101),  # Trait de código limpio
            "BienDocumentado": np.random.randint(0, 101),  # Trait de buena documentación
            "GITGod": np.random.randint(0, 101),  # Trait de dominio de GIT
            "Arquitecto": np.random.randint(0, 101),  # Trait de arquitectura
            "Detallista": np.random.randint(0, 101),  # Trait de atención al detalle
        }
        
        # Calcular puntuación total basada en traits
        self._calculate_total_score()
        
        # Registrar creación del héroe con traits en el log
        logging.info(f"Héroe creado: {self.name} {self.last_name} - Traits: {self.traits}")


    # metodo para calcular la puntuación total del héroe
    def _calculate_total_score(self):
        try:
            # Cálculo ponderado segun los pesos que me ha dado la gana ponerle
            weights = {
                "CodigoLimpio": 0.25,
                "BienDocumentado": 0.2,
                "GITGod": 0.2,
                "Arquitecto": 0.2,
                "Detallista": 0.15
            }
            
            # Calcular puntuación total basada en traits ponderados (se que este sum no lo hemos visto pero me gusta y lo pongo, es un poco como el .keys de javascript)
            self.points = sum(self.traits[trait] * weights[trait] for trait in self.traits)
            
            logging.info(f"Puntuación total calculada para héroe {self.name}: {self.points}")
            
        except Exception as e:
            logging.error(f"Error calculando puntuación para héroe {self.name}: {e}")
            self.points = 0

    # Metodo para obtener el valor de un trait específico
    def get_trait_value(self, trait_name):
        return self.traits.get(trait_name)

    # Metodo para representar el héroe como string
    def __str__(self):
        """Representación en string del héroe"""
        traits_str = ", ".join([f"{trait}: {value}" for trait, value in self.traits.items()])
        return f"HÉROE - {super().__str__()} | Traits: {traits_str}"
