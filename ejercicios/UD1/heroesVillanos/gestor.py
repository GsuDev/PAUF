import random
import logging
from datetime import datetime
from heroe import Heroe
from villano import Villano



"""
    Sistema principal de gestión de personajes para héroes y villanos
    Maneja creación, almacenamiento, búsqueda y emparejamiento de personajes
"""
class GestorPersonajes:
    
    # Constructor del gestor de personajes
    def __init__(self):
        # Inicializar el gestor de personajes con listas vacías
        self.heroes = []  # Lista para almacenar todos los héroes
        self.villains = []  # Lista para almacenar todos los villanos
        
        # Configurar sistema de logging
        self._setup_logging()
        
        logging.info("Gestor de Personajes inicializado")

    # Metodo privado para configurar el logging
    def _setup_logging(self):
        # Configura para que cree un archivo de log 
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                # Cuidado aquí si lo pruebas con la ruta que en Mac hay que ponerlo así pero igual a ti te da error
                logging.FileHandler('heroes_villains.log'),
                logging.StreamHandler()
            ]
        )

    # Metodo para crear un nuevo héroe
    def create_hero(self, name, last_name, birth_date):
        try:
            # Lo instancia
            hero = Heroe(name, last_name, birth_date)
            # Lo añade a la lista de héroes
            self.heroes.append(hero)
            logging.info(f"Héroe añadido exitosamente al sistema: {hero.name} {hero.last_name}")
            
            # Devuelve el héroe creado
            return hero
        except Exception as e:
            logging.error(f"Error creando héroe {name} {last_name}: {e}")
            return None

    # Metodo para crear un nuevo villano
    def create_villain(self, name, last_name, birth_date):
        try:
            # Lo instancia
            villain = Villano(name, last_name, birth_date)
            # Lo añade a la lista de villanos
            self.villains.append(villain)
            logging.info(f"Villano añadido exitosamente al sistema: {villain.name} {villain.last_name}")
            
            # Devuelve el villano creado
            return villain
        except Exception as e:
            logging.error(f"Error creando villano {name} {last_name}: {e}")
            return None

    # Metodo para buscar héroes por cualquier atributo o trait
    def search_heroes_by_attribute(self, attribute, value, comparison="equal"):
        try:
            # Crea una lista para almacenar los resultados
            results = []
            
            # Recorre todos los héroes
            for hero in self.heroes:
                # Buscar en atributos básicos
                if hasattr(hero, attribute):
                    attr_value = getattr(hero, attribute)
                    # Si coincide el valor según el tipo de comparación, lo añade a resultados
                    if self._compare_values(attr_value, value, comparison):
                        results.append(hero)
                # Buscar en traits
                elif attribute in hero.traits:
                    trait_value = hero.traits[attribute]
                    # Si coincide el valor según el tipo de comparación, lo añade a resultados
                    if self._compare_values(trait_value, value, comparison):
                        results.append(hero)
            
            logging.info(f"Búsqueda de héroes completada: {len(results)} resultados encontrados para {attribute} {comparison} {value}")
            
            # Devuelve la lista de resultados
            return results
            
        except Exception as e:
            logging.error(f"Error buscando héroes: {e}")
            return []

    # Metodo para buscar villanos por cualquier atributo o trait (similar al de héroes)
    def search_villains_by_attribute(self, attribute, value, comparison="equal"):
        try:
            # Crea una lista para almacenar los resultados
            results = []
            
            for villain in self.villains:
                # Buscar en atributos básicos
                if hasattr(villain, attribute):
                    attr_value = getattr(villain, attribute)
                    # Si coincide el valor según el tipo de comparación, lo añade a resultados
                    if self._compare_values(attr_value, value, comparison):
                        results.append(villain)
                # Buscar en traits
                elif attribute in villain.traits:
                    trait_value = villain.traits[attribute]
                    # Si coincide el valor según el tipo de comparación, lo añade a resultados
                    if self._compare_values(trait_value, value, comparison):
                        results.append(villain)
            
            logging.info(f"Búsqueda de villanos completada: {len(results)} resultados encontrados para {attribute} {comparison} {value}")
            
            # Devuelve la lista de resultados
            return results
            
        except Exception as e:
            logging.error(f"Error buscando villanos: {e}")
            return [] 

    # Metodo auxiliar para comparar valores basado en el tipo de comparación (para evitar repetir código)
    def _compare_values(self, attr_value, search_value, comparison):
        try:
            if comparison == "greater":
                return float(attr_value) > float(search_value)
            elif comparison == "less":
                return float(attr_value) < float(search_value)
            else:
                # Si no reconoce el tipo de comparación, asume igualdad (para string cae aqui)
                return attr_value == search_value
        except (ValueError, TypeError):
            # Si no puede convertir a float (por ejemplo, es un string pero han puesto tipo de comparacion), compara como strings
            return str(attr_value).lower() == str(search_value).lower()

    # Metodo para emparejar aleatoriamente un héroe y un villano
    def pair_random_characters(self):
        try:
            # Verificar que hay al menos un héroe y un villano
            if not self.heroes or not self.villains:
                logging.warning("No se puede crear parejas: No hay suficientes héroes o villanos")
                return {"error": "No hay suficientes héroes o villanos para crear una pareja"}
            
            # Seleccionar héroe y villano aleatorios
            hero = random.choice(self.heroes)
            villain = random.choice(self.villains)
            
            # Calcular diferencia de puntuación (valor absoluto)
            score_diff = abs(hero.points - villain.points)
            
            # Determinar si el enfrentamiento está equilibrado
            # Se considera equilibrado si la diferencia de puntuación es menor a 15 puntos
            is_balanced = score_diff < 15
            has_high_deviation = score_diff > 30
            
            # Crear diccionario de resultados (Así puedo devolver más info)
            result = {
                "hero": hero,
                "villain": villain,
                "hero_score": hero.points,
                "villain_score": villain.points,
                "score_difference": score_diff,
                "is_balanced": is_balanced,
                "has_high_deviation": has_high_deviation,
                "evaluation": self._get_match_evaluation(score_diff)
            }
            
            logging.info(f"Emparejamiento aleatorio creado: {hero.name} vs {villain.name} - "
                        f"Diferencia de puntuación: {score_diff:.2f} - {result['evaluation']}")
            
            return result
            
        except Exception as e:
            logging.error(f"Error creando pareja aleatoria: {e}")
            return {"error": f"Error creando pareja: {e}"}

    # Metodo auxiliar para evaluar el enfrentamiento basado en la diferencia de puntuación (para simplificar el metodo de emparejamiento)
    def _get_match_evaluation(self, score_diff):
        if score_diff < 10:
            return "Enfrentamiento perfectamente equilibrado"
        elif score_diff < 20:
            return "Enfrentamiento bien equilibrado"
        elif score_diff < 35:
            return "Desequilibrio moderado"
        else:
            return "Alta desviación - Enfrentamiento muy desequilibrado"

    # Metodo para obtener todos los héroes
    def get_all_heroes(self):
        logging.info(f"Obtenidos todos los héroes: {len(self.heroes)} héroes encontrados")
        return self.heroes

    # Metodo para obtener todos los villanos
    def get_all_villains(self):
        logging.info(f"Obtenidos todos los villanos: {len(self.villains)} villanos encontrados")
        return self.villains

    # Metodo para buscar un personaje (héroe o villano) por su ID único
    def get_character_by_id(self, char_id):
        try:
            # Buscar en héroes
            for hero in self.heroes:
                if hero.id == char_id:
                    logging.info(f"Héroe encontrado por ID {char_id}: {hero.name} {hero.last_name}")
                    return hero
            
            # Buscar en villanos
            for villain in self.villains:
                if villain.id == char_id:
                    logging.info(f"Villano encontrado por ID {char_id}: {villain.name} {villain.last_name}")
                    return villain
            
            
            # Si no se encuentra, devuelve None
            logging.warning(f"No se encontró personaje con ID {char_id}")
            return None
            
        except Exception as e:
            logging.error(f"Error buscando personaje por ID {char_id}: {e}")
            return None

    # Metodo para obtener estadísticas del sistema
    def get_statistics(self):
        try:
            stats = {
                "total_heroes": len(self.heroes),
                "total_villains": len(self.villains),
                "total_characters": len(self.heroes) + len(self.villains),
                "average_hero_score": sum(h.points for h in self.heroes) / len(self.heroes) if self.heroes else 0,
                "average_villain_score": sum(v.points for v in self.villains) / len(self.villains) if self.villains else 0
            }
            
            logging.info(f"Estadísticas calculadas: {stats}")
            return stats
            
        except Exception as e:
            logging.error(f"Error calculando estadísticas: {e}")
            return {}