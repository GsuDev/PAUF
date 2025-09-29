# Heroes and Villains Management System

> Readme Hecho con IA pasandole el proyecto

Sistema de gestión de héroes y villanos desarrollado en Python aplicando conceptos de Programación Orientada a Objetos (POO), manejo de estructuras de datos, búsquedas, aleatoriedad y logging.

## Características del Sistema

### Clases Principales

#### 1. Persona (Clase Base)
Contiene los atributos comunes para todos los personajes:
- **Nombre**: Nombre del personaje
- **Apellidos**: Apellidos del personaje  
- **Fecha de nacimiento**: En formato 'YYYY-MM-DD'
- **Identificador**: ID único autogenerado
- **Puntuación total**: Calculada según las cualidades
- **Cálculo de edad**: Basado en la fecha de nacimiento

#### 2. Villano
Hereda de Persona e incluye las siguientes cualidades negativas (0-100):
- **Chagepeteador**: Tendencia a copiar código
- **EntregadorTardio**: Retraso en entregas
- **Ausencias**: Faltas de asistencia
- **Hablador**: Hablar excesivamente

#### 3. Heroe  
Hereda de Persona e incluye las siguientes cualidades positivas (0-100):
- **CodigoLimpio**: Calidad del código
- **BienDocumentado**: Documentación del código
- **GITGod**: Dominio de Git
- **Arquitecto**: Habilidades de arquitectura
- **Detallista**: Atención al detalle

#### 4. GestorPersonajes
Clase principal que gestiona todo el sistema:
- Creación dinámica de héroes y villanos
- Almacenamiento en listas
- Sistema de búsquedas avanzadas
- Emparejamiento aleatorio
- Evaluación de equilibrio en combates
- Logging completo de todas las operaciones

## Funcionalidades

### Sistema de Puntuación
- Utiliza un algoritmo similar al de FIFA
- **Villanos**: Penalización basada en traits negativos
- **Héroes**: Puntuación basada en traits positivos
- Pesos específicos para cada cualidad

### Sistema de Búsquedas
Permite búsquedas por cualquier atributo o cualidad:
- **Por nombre**: `search_heroes_by_attribute("name", "Juan")`
- **Por cualidad específica**: `search_heroes_by_attribute("GITGod", 50, "greater")`
- **Por puntuación**: `search_villains_by_attribute("points", 60, "less")`
- **Tipos de comparación**: "equal", "greater", "less"

### Sistema de Emparejamiento
- Emparejamiento aleatorio entre héroes y villanos
- Evaluación automática del equilibrio del combate:
  - **Equilibrado**: Diferencia < 15 puntos
  - **Desequilibrio moderado**: Diferencia 15-35 puntos  
  - **Alta desviación**: Diferencia > 35 puntos

### Sistema de Logging
- Registro completo de todas las operaciones
- Archivos de log: `heroes_villains.log`
- Información de errores y excepciones
- Trazabilidad completa del sistema

## Instalación y Uso

### Requisitos
```bash
pip install -r requirements.txt
```

### Ejecución
```bash
python main.py
```

### Estructura de Archivos
```
proyecto/
├── persona.py          # Clase base Persona
├── heroe.py           # Clase Heroe
├── villano.py         # Clase Villano
├── gestor.py          # Gestor principal del sistema
├── main.py            # Programa principal de demostración
├── requirements.txt   # Dependencias
├── README.md         # Esta documentación
└── heroes_villains.log # Archivo de logs (generado automáticamente)
```

## Ejemplos de Uso

### Crear Personajes
```python
from gestor import GestorPersonajes

manager = GestorPersonajes()

# Crear héroe
hero = manager.create_hero("Juan", "Pérez", "1995-03-15")

# Crear villano
villain = manager.create_villain("Fernando", "García", "1992-07-22")
```

### Realizar Búsquedas
```python
# Buscar héroes por nombre
heroes = manager.search_heroes_by_attribute("name", "Juan")

# Buscar villanos con Chagepeteador > 70
villains = manager.search_villains_by_attribute("Chagepeteador", 70, "greater")

# Buscar héroes con GITGod > 50
git_heroes = manager.search_heroes_by_attribute("GITGod", 50, "greater")
```

### Emparejar Personajes
```python
# Crear emparejamiento aleatorio
pairing = manager.pair_random_characters()

print(f"Héroe: {pairing['hero'].name}")
print(f"Villano: {pairing['villain'].name}")
print(f"Evaluación: {pairing['evaluation']}")
print(f"¿Equilibrado?: {pairing['is_balanced']}")
```

### Obtener Estadísticas
```python
stats = manager.get_statistics()
print(f"Total de héroes: {stats['total_heroes']}")
print(f"Total de villanos: {stats['total_villains']}")
print(f"Puntuación promedio héroes: {stats['average_hero_score']:.2f}")
```

## Algoritmo de Puntuación

### Para Villanos
```
Puntuación = 100 - (Chagepeteador * 0.3 + EntregadorTardio * 0.25 + 
                    Ausencias * 0.25 + Hablador * 0.2)
```

### Para Héroes  
```
Puntuación = CodigoLimpio * 0.25 + BienDocumentado * 0.2 + 
             GITGod * 0.2 + Arquitecto * 0.2 + Detallista * 0.15
```

## Características Técnicas

- **POO**: Herencia, encapsulación y polimorfismo
- **Manejo de excepciones**: Try-catch en todas las operaciones críticas
- **Logging**: Sistema completo de trazabilidad
- **Aleatoriedad**: Generación de traits y emparejamientos aleatorios
- **Búsquedas flexibles**: Por cualquier atributo con diferentes comparadores
- **Validación de datos**: Verificación de formatos y valores

## Logging

El sistema genera logs detallados que incluyen:
- Creación de personajes
- Cálculo de puntuaciones
- Operaciones de búsqueda
- Emparejamientos realizados
- Errores y excepciones
- Estadísticas del sistema

## Autor

Desarrollado para la práctica "Héroes y Villanos del Virgen" - CIFP Virgen de Gracia

## Notas de Entrega

- Fecha límite: 29/09/2025
- Entrega por GIT en carpeta personal
- Incluir PDF con enlace al repositorio
- El código debe poder ser defendido oralmente