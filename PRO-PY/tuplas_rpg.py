# =====================================================================
#  TUPLAS EN PYTHON - GUÍA DE AVENTURA RPG
# =====================================================================
#
#  CÓMO USAR ESTE ARCHIVO
#  ----------------------
#  1. Ábrelo en Thonny (o en tu editor) y pulsa "Ejecutar".
#  2. Verás los resultados en la consola, en el mismo orden del archivo.
#  3. Cada print tiene un comentario "# Salida:" que dice QUÉ va a salir.
#     Compara lo que esperas con lo que sale. Si coincide, lo has entendido.
#  4. Todo lo que empieza por # es un comentario: Python lo ignora.
#     Son notas para ti.
#  5. Si ya viste la guía de listas, aquí muchas cosas te sonarán igual.
#     Lo importante de este archivo es ENTENDER QUÉ SE PUEDE Y QUÉ NO
#     SE PUEDE HACER con una tupla, y POR QUÉ.
#
#  ESTRUCTURA (siempre igual en cada sección):
#     - QUÉ ES: la idea explicada con palabras sencillas
#     - EJEMPLO: código que puedes ejecutar
#     - ATENCIÓN: errores típicos y trampas
#
#  SOBRE LOS ERRORES
#  -----------------
#  Algunos ejemplos provocan errores A PROPÓSITO para que veas cómo son.
#  Para que el programa no se pare, uso este bloque:
#
#      try:
#          (código que puede fallar)
#      except TipoDeError as error:
#          (qué hacer si falla)
#
#  Se lee así: "INTENTA hacer esto. Si falla con este tipo de error,
#  haz esto otro en vez de detener todo el programa".
#  Los textos exactos de los errores pueden variar un poco según tu
#  versión de Python. Lo importante es el TIPO de error.
#
#  ÍNDICE
#     1. Qué es una tupla
#     2. Crear tuplas (y la trampa de un solo elemento)
#     3. Pertenencia: in / not in
#     4. Concatenar (+) y repetir (*)
#     5. Indexación: acceder a un elemento
#     6. Slicing: cortar trozos de una tupla
#     7. Tamaño y extremos: len, min, max, sum
#     8. sorted(): ordenar (devuelve una LISTA)
#     9. Buscar: index() y count()
#    10. Lo que NO se puede hacer: la inmutabilidad
#    11. Cómo "modificar" una tupla (el truco de la lista)
#    12. Tuplas anidadas
#    13. La trampa: una lista dentro de una tupla
#    14. Desempaquetado (y el intercambio de variables)
#    15. Tuplas y funciones: devolver varios valores
#    16. Crear tuplas con tuple()
#    17. Comparar tuplas: == frente a is
#    18. Tuplas frente a listas: cuándo usar cada una
#    19. Resumen final y reto
# =====================================================================


# =====================================================================
# 1. QUÉ ES UNA TUPLA
# =====================================================================
# QUÉ ES:
#   Una tupla es una colección ORDENADA de elementos, como una lista,
#   pero con una diferencia enorme:
#
#       UNA TUPLA NO SE PUEDE MODIFICAR después de crearla.
#       (A esto se le llama "inmutable".)
#
#   Se escribe normalmente con paréntesis ( ) y los elementos se
#   separan con comas.
#
# ANALOGÍA RPG:
#   - Una LISTA es tu inventario: añades, quitas y cambias objetos.
#   - Una TUPLA es la FICHA BASE de un jefe final o las coordenadas de
#     una ciudad: son datos fijos que el juego no debe cambiar por
#     accidente. Están "grabados en piedra".
#
# REGLAS IMPORTANTES:
#   - Los elementos están ORDENADOS: cada uno tiene una posición fija.
#   - Los elementos se pueden REPETIR.
#   - Una tupla es INMUTABLE: no puedes añadir, quitar ni cambiar
#     elementos.
#   - Los elementos pueden ser de distintos tipos.
#   - La PRIMERA posición es la 0, igual que en las listas.

print("=== 1. QUÉ ES UNA TUPLA ===")

boss = ('Sephiroth', 99, 'Espada Masamune')   # Nombre, nivel, arma
print(boss)              # Salida: ('Sephiroth', 99, 'Espada Masamune')
print(type(boss))        # Salida: <class 'tuple'>
print()


# =====================================================================
# 2. CREAR TUPLAS (Y LA TRAMPA DE UN SOLO ELEMENTO)
# =====================================================================
# QUÉ ES:
#   Hay varias formas de escribir una tupla:
#   - Con paréntesis y comas:      (1, 2, 3)
#   - Sin paréntesis, solo comas:  1, 2, 3   (también es una tupla)
#   - Vacía:                       ()
#   - De UN elemento:              (5,)   <- la coma final es OBLIGATORIA
#
# ATENCIÓN (la trampa más famosa de las tuplas):
#   Lo que crea la tupla es la COMA, no los paréntesis.
#   - ('Link')  -> NO es una tupla. Son paréntesis normales alrededor
#                  de un texto, y el resultado es un simple texto.
#   - ('Link',) -> SÍ es una tupla de un elemento (fíjate en la coma).

print("=== 2. CREAR TUPLAS ===")

coords = (10, 25)                 # Con paréntesis
print(coords)                     # Salida: (10, 25)

coords2 = 10, 25                  # Sin paréntesis: también es una tupla
print(coords2)                    # Salida: (10, 25)
print(type(coords2))              # Salida: <class 'tuple'>

empty = ()                        # Tupla vacía
print(empty)                      # Salida: ()
print(len(empty))                 # Salida: 0

not_a_tuple = ('Link')            # ¡Sin coma! Es solo un texto
print(type(not_a_tuple))          # Salida: <class 'str'>

one_item = ('Link',)              # Con coma: tupla de un elemento
print(type(one_item))             # Salida: <class 'tuple'>
print(one_item)                   # Salida: ('Link',)
print()


# =====================================================================
# 3. PERTENENCIA: in / not in
# =====================================================================
# QUÉ ES:
#   Pregunta "¿este elemento está en la tupla?".
#   - in      -> True si está, False si no está.
#   - not in  -> True si NO está, False si está.
#
# ANALOGÍA RPG:
#   Mirar la ficha de un personaje y preguntar: "¿tiene la habilidad
#   Fuego?".

print("=== 3. PERTENENCIA: in / not in ===")

skills = ('Fuego', 'Hielo', 'Rayo', 'Cura')

print('Fuego' in skills)          # Salida: True
print('Veneno' in skills)         # Salida: False
print('Veneno' not in skills)     # Salida: True
print('fuego' in skills)          # Salida: False  (mayúsculas y minúsculas importan)
print()


# =====================================================================
# 4. CONCATENAR (+) Y REPETIR (*)
# =====================================================================
# QUÉ ES:
#   - Con +  unes dos tuplas en una tupla NUEVA.
#   - Con *  repites el contenido de una tupla varias veces.
#
# ATENCIÓN:
#   Como las tuplas no se pueden modificar, estas operaciones NUNCA
#   cambian las originales. Crean una tupla nueva.
#   Solo puedes unir tupla con tupla (no tupla con lista).

print("=== 4. CONCATENAR (+) Y REPETIR (*) ===")

basic_skills = ('Fuego', 'Hielo')
advanced_skills = ('Rayo', 'Cura')

all_skills = basic_skills + advanced_skills
print(all_skills)             # Salida: ('Fuego', 'Hielo', 'Rayo', 'Cura')
print(basic_skills * 2)       # Salida: ('Fuego', 'Hielo', 'Fuego', 'Hielo')
print(basic_skills)           # Salida: ('Fuego', 'Hielo')  (la original NO cambió)

# Error a propósito: unir una tupla con una lista.
try:
    print(basic_skills + ['Rayo'])
except TypeError as error:
    print("Error:", error)    # Salida: Error: can only concatenate tuple (not "list") to tuple
print()


# =====================================================================
# 5. INDEXACIÓN: ACCEDER A UN ELEMENTO
# =====================================================================
# QUÉ ES:
#   Igual que en las listas: nombre_de_la_tupla[índice].
#   El primero es el 0. Los índices negativos cuentan desde el final
#   (-1 es el último).
#
# TABLA de la tupla 'party_stats' (5 elementos):
#
#   Elemento:   'Link'  120   45   30   'Espada'
#   Índice +:     0      1     2    3      4
#   Índice -:    -5     -4    -3   -2     -1
#
# ATENCIÓN: un índice que no existe da IndexError.

print("=== 5. INDEXACIÓN ===")

hero = ('Link', 120, 45, 30, 'Espada')   # Nombre, vida, ataque, defensa, arma

print(hero[0])     # Salida: Link
print(hero[1])     # Salida: 120
print(hero[-1])    # Salida: Espada
print(hero[-2])    # Salida: 30

try:
    print(hero[5])    # Solo existen los índices 0 a 4
except IndexError as error:
    print("Error:", error)    # Salida: Error: tuple index out of range
print()


# =====================================================================
# 6. SLICING: CORTAR TROZOS DE UNA TUPLA
# =====================================================================
# QUÉ ES:
#   Igual que en las listas:  tupla[inicio : fin : paso]
#   - inicio: primer índice que se INCLUYE.
#   - fin:    índice donde se PARA. Ese índice NO se incluye.
#   - paso:   de cuánto en cuánto se avanza.
#
# DIFERENCIA con las listas: el resultado es otra TUPLA (no una lista).
#
# ATENCIÓN: un slice nunca da error por pasarte del final.

print("=== 6. SLICING ===")

# Recordatorio: hero = ('Link', 120, 45, 30, 'Espada')

print(hero[0:3])      # Salida: ('Link', 120, 45)  (índices 0, 1, 2)
print(hero[2:])       # Salida: (45, 30, 'Espada')  (del 2 al final)
print(hero[:2])       # Salida: ('Link', 120)  (del principio al 1)
print(hero[::2])      # Salida: ('Link', 45, 'Espada')  (índices 0, 2, 4)
print(hero[::-1])     # Salida: ('Espada', 30, 45, 120, 'Link')  (al revés)
print(hero[3:100])    # Salida: (30, 'Espada')  (no da error)
print()


# =====================================================================
# 7. TAMAÑO Y EXTREMOS: len, min, max, sum
# =====================================================================
# QUÉ ES:
#   - len(tupla): cuántos elementos tiene.
#   - min(tupla): el menor.   max(tupla): el mayor.
#   - sum(tupla): la suma (SOLO si todos son números).
#
# ATENCIÓN: min, max y sum no funcionan si mezclas textos y números
#   (por ejemplo, la tupla 'hero' de arriba daría TypeError).

print("=== 7. TAMAÑO Y EXTREMOS ===")

damage_rolls = (12, 8, 20, 5, 17)    # Resultados de tiradas de daño

print(len(damage_rolls))     # Salida: 5
print(min(damage_rolls))     # Salida: 5
print(max(damage_rolls))     # Salida: 20
print(sum(damage_rolls))     # Salida: 62   (12 + 8 + 20 + 5 + 17)

print(min(skills))           # Salida: Cura  (primero alfabéticamente)
print(max(skills))           # Salida: Rayo  (último alfabéticamente)
print()


# =====================================================================
# 8. sorted(): ORDENAR (DEVUELVE UNA LISTA)
# =====================================================================
# QUÉ ES:
#   sorted(tupla) devuelve una LISTA NUEVA ordenada.
#
# ATENCIÓN (diferencia importante con las listas):
#   - Una tupla NO tiene el método .sort(), porque ordenar la
#     modificaría y las tuplas no se pueden modificar.
#   - sorted() SIEMPRE devuelve una LISTA, aunque le des una tupla.
#   - Si quieres el resultado como tupla: tuple(sorted(tupla)).

print("=== 8. sorted() ===")

print(sorted(damage_rolls))
# Salida: [5, 8, 12, 17, 20]   (¡fíjate: corchetes, es una lista!)

print(sorted(damage_rolls, reverse=True))
# Salida: [20, 17, 12, 8, 5]

print(tuple(sorted(damage_rolls)))
# Salida: (5, 8, 12, 17, 20)   (convertida de nuevo en tupla)

print(damage_rolls)
# Salida: (12, 8, 20, 5, 17)   (la original NO cambió)

try:
    damage_rolls.sort()
except AttributeError as error:
    print("Error:", error)
    # Salida: Error: 'tuple' object has no attribute 'sort'
print()


# =====================================================================
# 9. BUSCAR: index() Y count()
# =====================================================================
# QUÉ ES:
#   Las tuplas SOLO tienen dos métodos propios:
#   - tupla.index(x): posición de la primera aparición de x.
#   - tupla.count(x): cuántas veces aparece x.
#   index() también acepta "desde" y "hasta" igual que en las listas.
#
# ATENCIÓN: si x no está, index() da ValueError. count() devuelve 0.
#
# ¿POR QUÉ SOLO DOS MÉTODOS?
#   Porque los demás métodos de las listas (append, remove, pop,
#   sort...) sirven para MODIFICAR, y las tuplas no se modifican.

print("=== 9. index() y count() ===")

enemies = ('Slime', 'Goblin', 'Slime', 'Dragón', 'Slime')
# Índices:    0        1         2        3         4

print(enemies.index('Slime'))         # Salida: 0
print(enemies.index('Dragón'))        # Salida: 3
print(enemies.index('Slime', 1))      # Salida: 2  (buscando desde el índice 1)
print(enemies.index('Slime', 3))      # Salida: 4
print(enemies.count('Slime'))         # Salida: 3
print(enemies.count('Beholder'))      # Salida: 0

try:
    print(enemies.index('Beholder'))
except ValueError as error:
    print("Error:", error)    # Salida: Error: tuple.index(x): x not in tuple
print()


# =====================================================================
# 10. LO QUE NO SE PUEDE HACER: LA INMUTABILIDAD
# =====================================================================
# QUÉ ES:
#   "Inmutable" significa que, una vez creada, la tupla no puede
#   cambiar. Python lo impide con un error.
#
#   NO se puede:
#   - Cambiar un elemento:   tupla[0] = 'x'     -> TypeError
#   - Borrar un elemento:    del tupla[0]       -> TypeError
#   - Añadir:                tupla.append('x')  -> AttributeError
#   - Quitar:                tupla.remove('x')  -> AttributeError
#
#   SÍ se puede:
#   - Leer, buscar, contar, cortar y recorrer.
#   - Borrar la tupla ENTERA con  del tupla.
#   - Reasignar el NOMBRE a otra tupla distinta (ver sección 11).
#
# ¿PARA QUÉ SIRVE QUE NO SE PUEDA CAMBIAR?
#   Para proteger datos que no deben alterarse por accidente:
#   coordenadas fijas, colores, fechas, estadísticas base de un jefe...
#   Si algún día un fallo en tu programa intenta cambiarlos, Python
#   avisa con un error en vez de corromper los datos en silencio.

print("=== 10. INMUTABILIDAD ===")

final_boss = ('Sephiroth', 99, 'Masamune')

try:
    final_boss[1] = 50           # Intentar bajarle el nivel al jefe final
except TypeError as error:
    print("Error:", error)       # Salida: Error: 'tuple' object does not support item assignment

try:
    del final_boss[0]            # Intentar borrar un elemento
except TypeError as error:
    print("Error:", error)       # Salida: Error: 'tuple' object doesn't support item deletion

try:
    final_boss.append('Alas')    # Intentar añadir un elemento
except AttributeError as error:
    print("Error:", error)       # Salida: Error: 'tuple' object has no attribute 'append'

print(final_boss)                # Salida: ('Sephiroth', 99, 'Masamune')  (intacto)
print()


# =====================================================================
# 11. CÓMO "MODIFICAR" UNA TUPLA (EL TRUCO DE LA LISTA)
# =====================================================================
# QUÉ ES:
#   Si de verdad necesitas un cambio, hay dos caminos. En ambos NO se
#   modifica la tupla original: se crea una NUEVA.
#
#   CAMINO A: tupla -> lista -> modificar -> tupla
#       1. list(tupla)   convierte la tupla en lista.
#       2. Modificas la lista como quieras.
#       3. tuple(lista)  la vuelve a convertir en tupla.
#
#   CAMINO B: concatenar y/o hacer slices para construir una nueva:
#       nueva = tupla[:1] + ('algo',) + tupla[2:]
#
# ANALOGÍA RPG:
#   Tienes la ficha oficial grabada en piedra. Para "cambiarla", haces
#   una copia en papel (lista), la editas y grabas una piedra NUEVA.

print("=== 11. 'MODIFICAR' UNA TUPLA ===")

stats = ('Link', 120, 45)
print(stats)                       # Salida: ('Link', 120, 45)

# Camino A
stats_list = list(stats)           # Paso 1: tupla -> lista
stats_list[1] = 150                # Paso 2: modificar la lista
stats = tuple(stats_list)          # Paso 3: lista -> tupla (y reasignamos el nombre)
print(stats)                       # Salida: ('Link', 150, 45)

# Camino B: sustituir el elemento 2 (el 45) por 60
stats = stats[:2] + (60,)          # Fíjate en la coma: (60,) es una tupla de un elemento
print(stats)                       # Salida: ('Link', 150, 60)

# Añadir un elemento al final con +
stats = stats + ('Espada',)
print(stats)                       # Salida: ('Link', 150, 60, 'Espada')
print()


# =====================================================================
# 12. TUPLAS ANIDADAS
# =====================================================================
# QUÉ ES:
#   Una tupla puede contener otras tuplas. Se accede con dos índices:
#       tupla[índice_exterior][índice_interior]
#
# ANALOGÍA RPG:
#   Una ruta de viaje fija: cada parada es una tupla (nombre, x, y) y
#   la ruta completa es una tupla de paradas.

print("=== 12. TUPLAS ANIDADAS ===")

route = (
    ('Aldea Kokiri', 10, 5),     # Parada 0
    ('Bosque Perdido', 25, 12),  # Parada 1
    ('Castillo', 40, 30),        # Parada 2
)

print(route[0])         # Salida: ('Aldea Kokiri', 10, 5)
print(route[1][0])      # Salida: Bosque Perdido  (parada 1, elemento 0)
print(route[2][-1])     # Salida: 30              (parada 2, último elemento)
print(len(route))       # Salida: 3  (hay 3 paradas)
print()


# =====================================================================
# 13. LA TRAMPA: UNA LISTA DENTRO DE UNA TUPLA
# =====================================================================
# QUÉ ES:
#   La tupla es inmutable, pero SOLO en lo que ella guarda directamente.
#   Si dentro hay un objeto MUTABLE (como una lista), ESE objeto sí
#   puede cambiar.
#
#   La tupla guarda "la dirección" de la lista, y esa dirección no
#   cambia. Pero el CONTENIDO de la lista sí puede cambiar.
#
# ANALOGÍA RPG:
#   Una caja de cristal sellada (la tupla) que contiene una mochila
#   (la lista). No puedes cambiar la mochila por otra, pero SÍ puedes
#   meter y sacar cosas dentro de la mochila.
#
# RECOMENDACIÓN: para que sea de verdad inmutable, evita listas dentro
#   de tuplas.

print("=== 13. LISTA DENTRO DE UNA TUPLA ===")

character = ('Cloud', ['Espada', 'Poción'])   # La segunda posición es una lista

# No puedo cambiar QUÉ hay en la posición 1:
try:
    character[1] = ['Otra cosa']
except TypeError as error:
    print("Error:", error)         # Salida: Error: 'tuple' object does not support item assignment

# Pero SÍ puedo modificar el CONTENIDO de la lista que hay dentro:
character[1].append('Materia')
print(character)                   # Salida: ('Cloud', ['Espada', 'Poción', 'Materia'])
print()


# =====================================================================
# 14. DESEMPAQUETADO (Y EL INTERCAMBIO DE VARIABLES)
# =====================================================================
# QUÉ ES:
#   Repartir los elementos de una tupla en VARIAS variables en una
#   sola línea. Es una de las cosas que más se usan con tuplas.
#
# REGLA: el número de variables debe coincidir con el número de
#   elementos, si no da ValueError.
#
# ESTRELLA (*): una variable con * recoge "todo lo que sobre" y lo
#   guarda como LISTA (no como tupla).
#
# TRUCO DE INTERCAMBIO: a, b = b, a
#   Intercambia dos variables sin necesitar una variable auxiliar.
#   Funciona porque "b, a" es una tupla que se desempaqueta.

print("=== 14. DESEMPAQUETADO ===")

name, level, weapon = ('Sephiroth', 99, 'Masamune')
print(name)       # Salida: Sephiroth
print(level)      # Salida: 99
print(weapon)     # Salida: Masamune

# Error a propósito: 2 variables para 3 elementos.
try:
    a, b = ('Sephiroth', 99, 'Masamune')
except ValueError as error:
    print("Error:", error)    # Salida: Error: too many values to unpack (expected 2)

# Con estrella:
first, *rest = (10, 20, 30, 40)
print(first)      # Salida: 10
print(rest)       # Salida: [20, 30, 40]   (¡es una lista!)

x, *middle, z = (1, 2, 3, 4, 5)
print(x)          # Salida: 1
print(middle)     # Salida: [2, 3, 4]
print(z)          # Salida: 5

# Intercambio de variables:
player_one = 'Mario'
player_two = 'Luigi'
player_one, player_two = player_two, player_one
print(player_one)    # Salida: Luigi
print(player_two)    # Salida: Mario
print()


# =====================================================================
# 15. TUPLAS Y FUNCIONES: DEVOLVER VARIOS VALORES
# =====================================================================
# QUÉ ES:
#   Una función es un bloque de código con nombre que puedes usar
#   cuando quieras. Se define con la palabra "def".
#   Una función puede devolver VARIOS valores a la vez: Python los
#   empaqueta automáticamente en una TUPLA.
#
#   (Si todavía no has visto funciones, no pasa nada. Fíjate solo en
#   que lo que sale es una tupla y se puede desempaquetar.)
#
#   def nombre():          <- crea la función
#       return a, b        <- devuelve dos valores (en una tupla)

print("=== 15. FUNCIONES QUE DEVUELVEN TUPLAS ===")


def roll_stats():
    # Devuelve vida, ataque y defensa de un personaje nuevo.
    return 100, 25, 10


result = roll_stats()
print(result)             # Salida: (100, 25, 10)
print(type(result))       # Salida: <class 'tuple'>

hp, attack, defense = roll_stats()    # Desempaquetamos directamente
print(hp)                 # Salida: 100
print(attack)             # Salida: 25
print(defense)            # Salida: 10
print()


# =====================================================================
# 16. CREAR TUPLAS CON tuple()
# =====================================================================
# QUÉ ES:
#   tuple(algo) convierte "algo que se puede recorrer" en una tupla:
#   una lista, un texto, un range...
#   Es la operación contraria a list().

print("=== 16. tuple() ===")

print(tuple(['Fuego', 'Hielo']))    # Salida: ('Fuego', 'Hielo')  (de lista a tupla)
print(tuple('Zelda'))               # Salida: ('Z', 'e', 'l', 'd', 'a')  (de texto a tupla)
print(tuple(range(5)))              # Salida: (0, 1, 2, 3, 4)
print(tuple())                      # Salida: ()  (tupla vacía)
print(list(('Link', 'Zelda')))      # Salida: ['Link', 'Zelda']  (de tupla a lista)
print()


# =====================================================================
# 17. COMPARAR TUPLAS: == FRENTE A is
# =====================================================================
# QUÉ ES:
#   - ==  pregunta: "¿tienen el MISMO CONTENIDO?"
#   - is  pregunta: "¿son EXACTAMENTE el MISMO OBJETO en la memoria?"
#
# NOTA: con tuplas pequeñas, Python a veces reutiliza el mismo objeto
#   por dentro, y entonces "is" puede dar True aunque las hayas escrito
#   dos veces. Es un detalle interno que NO debes usar en tus
#   programas. Para comparar contenido, usa SIEMPRE ==.
#
# El ORDEN importa al comparar.

print("=== 17. == frente a is ===")

pair_a = ('Link', 'Zelda')
pair_b = ('Link', 'Zelda')

print(pair_a == pair_b)                      # Salida: True   (mismo contenido)
print(('Link', 'Zelda') == ('Zelda', 'Link'))  # Salida: False  (distinto orden)
print()


# =====================================================================
# 18. TUPLAS FRENTE A LISTAS: CUÁNDO USAR CADA UNA
# =====================================================================
#
#   Característica         LISTA  [ ]                TUPLA  ( )
#   --------------------   -----------------------   -----------------------
#   Se puede modificar     Sí                        No
#   Escritura              [1, 2, 3]                 (1, 2, 3)
#   Un solo elemento       [5]                       (5,)   <- coma obligatoria
#   append / remove / pop  Sí                        No
#   sort() / reverse()     Sí                        No
#   index() / count()      Sí                        Sí
#   Slicing / in / len     Sí                        Sí
#   Uso típico             Datos que CAMBIAN         Datos FIJOS
#
#   REGLA PRÁCTICA:
#   - Inventario, grupo de héroes, enemigos de la sala  -> LISTA
#     (cambian durante el juego).
#   - Coordenadas, colores RGB, ficha base del jefe,
#     días de la semana                                 -> TUPLA
#     (no deben cambiar).

print("=== 18. EJEMPLO: LISTA FRENTE A TUPLA ===")

inventory = ['Poción', 'Espada']                  # LISTA: va a cambiar
inventory.append('Escudo')
print(inventory)          # Salida: ['Poción', 'Espada', 'Escudo']

red_color = (255, 0, 0)                           # TUPLA: un color fijo (R, G, B)
print(red_color)          # Salida: (255, 0, 0)
print()


# =====================================================================
# 19. RESUMEN FINAL Y RETO
# =====================================================================
# RESUMEN RÁPIDO (qué quiero hacer -> cómo se hace)
#
#  Quiero...                          Uso...
#  --------------------------------   ------------------------------
#  Crear una tupla                    (a, b, c)   o   a, b, c
#  Tupla de un elemento               (a,)        <- con coma
#  Saber si algo está                 x in tupla  /  x not in tupla
#  Unir dos tuplas                    tupla1 + tupla2
#  Repetir una tupla                  tupla * n
#  Ver un elemento                    tupla[i]
#  Cortar un trozo                    tupla[inicio:fin:paso]
#  Saber cuántos hay                  len(tupla)
#  Menor / mayor / suma               min(tupla) / max(tupla) / sum(tupla)
#  Ordenar (devuelve lista)           sorted(tupla)
#  Posición de un valor               tupla.index(x)
#  Contar apariciones                 tupla.count(x)
#  Repartir en variables              a, b, c = tupla
#  Convertir a lista / a tupla        list(tupla)  /  tuple(lista)
#  "Modificar" (creando una nueva)    lista intermedia, o + y slices
#
# ERRORES MÁS COMUNES (revisa esta lista si algo falla):
#   1. Escribir ('Link') en vez de ('Link',): sin coma no es tupla.
#   2. Intentar tupla[i] = valor (TypeError: las tuplas no se modifican).
#   3. Intentar usar append, remove, pop, sort... (AttributeError).
#   4. Esperar que sorted(tupla) devuelva una tupla (devuelve una lista).
#   5. Intentar unir una tupla con una lista usando + (TypeError).
#   6. Contar desde 1 en vez de desde 0.
#   7. Olvidar que en un slice el "fin" NO se incluye.
#   8. Creer que una lista dentro de una tupla también es inmutable.

print("=== 19. RETO FINAL ===")

# RETO (hazlo tú, escribiendo código debajo de cada punto):
#   1. Crea una tupla llamada 'boss' con 4 datos de un jefe final:
#      nombre, nivel, vida y arma.
#   2. Imprime solo el nombre y el arma usando índices.
#   3. Desempaqueta la tupla en 4 variables e imprime cada una.
#   4. Crea una tupla de un solo elemento con la habilidad 'Meteoro'.
#   5. Une esa tupla con ('Fuego', 'Hielo') en una nueva tupla.
#   6. Intenta cambiar boss[1] dentro de un try/except TypeError y
#      comprueba que sale el error.
#   7. Convierte 'boss' en lista, sube su nivel en 1 y conviértela de
#      nuevo en tupla. Imprime el resultado.
#
# Escribe tu solución aquí abajo:

print("¡Fin de la guía de tuplas! Has sellado la mazmorra.")
