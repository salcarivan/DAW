# =====================================================================
#  LISTAS EN PYTHON - GUÍA DE AVENTURA RPG
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
#  No necesitas dominarlo ahora. Solo entender que sirve para enseñar errores.
#
#  ÍNDICE
#     1. Qué es una lista
#     2. Pertenencia: in / not in
#     3. Concatenar (+) y repetir (*)
#     4. Indexación: acceder a un elemento
#     5. Modificar un elemento
#     6. Slicing: cortar trozos de una lista
#     7. Tamaño y extremos: len, min, max, sum
#     8. Ordenar sin tocar la original: sorted()
#     9. Buscar: index() y count()
#    10. Añadir: append(), extend(), insert()
#    11. Eliminar: remove(), del, pop(), clear()
#    12. reverse() y sort()
#    13. Copiar listas: copy(), list() y la trampa del "alias"
#    14. Comparar listas: == frente a is
#    15. Listas anidadas (listas dentro de listas)
#    16. Desempaquetado
#    17. Crear listas con list() y range()
#    18. Resumen final y reto
# =====================================================================


# =====================================================================
# 1. QUÉ ES UNA LISTA
# =====================================================================
# QUÉ ES:
#   Una lista es una colección ORDENADA de elementos guardados bajo un
#   solo nombre. Se escribe con corchetes [ ] y los elementos se
#   separan con comas.
#
# ANALOGÍA RPG:
#   Es como el INVENTARIO de un videojuego. Tiene casillas numeradas.
#   Cada casilla guarda un objeto. Puedes añadir, quitar, cambiar y
#   ordenar objetos.
#
# REGLAS IMPORTANTES:
#   - Los elementos están ORDENADOS: cada uno tiene una posición fija.
#   - Los elementos se pueden REPETIR (dos "Poción" son válidas).
#   - Una lista es MUTABLE: se puede modificar después de crearla.
#   - Los elementos pueden ser de distintos tipos (texto, números...).
#   - La PRIMERA posición es la 0, no la 1. (Muy importante.)

print("=== 1. QUÉ ES UNA LISTA ===")

party = ['Link', 'Cloud', 'Goku']   # Lista de tres héroes (textos)
print(party)                        # Salida: ['Link', 'Cloud', 'Goku']

mixed = ['Espada', 15, True]        # Texto, número entero y booleano
print(mixed)                        # Salida: ['Espada', 15, True]

empty = []                          # Lista vacía: inventario sin objetos
print(empty)                        # Salida: []

print(type(party))                  # Salida: <class 'list'>
print()


# =====================================================================
# 2. PERTENENCIA: in / not in
# =====================================================================
# QUÉ ES:
#   Sirve para preguntar "¿este elemento está en la lista?".
#   - in      -> True si está, False si no está.
#   - not in  -> True si NO está, False si está.
#
# ANALOGÍA RPG:
#   Es mirar tu grupo y preguntar: "¿Cloud está en mi equipo?".

print("=== 2. PERTENENCIA: in / not in ===")

print('Cloud' in party)             # Salida: True   (Cloud está en el grupo)
print('Sephiroth' in party)         # Salida: False  (Sephiroth no está)
print('Sephiroth' not in party)     # Salida: True   (no está, así que "not in" es True)

# ATENCIÓN: esta forma también funciona, pero es más confusa:
print(not 'Link' in party)          # Salida: False
# Paso a paso: 'Link' in party da True. Luego "not" invierte True a False.
# Recomendación: usa "not in", se lee más parecido al lenguaje normal.

# ATENCIÓN: mayúsculas y minúsculas importan.
print('link' in party)              # Salida: False  ('link' no es igual que 'Link')
print()


# =====================================================================
# 3. CONCATENAR (+) Y REPETIR (*)
# =====================================================================
# QUÉ ES:
#   - Con +  unes dos listas en una lista nueva.
#   - Con *  repites el contenido de una lista varias veces.
#
# ANALOGÍA RPG:
#   - "+" es fusionar dos grupos de aventureros en uno solo.
#   - "*" es comprar el mismo objeto varias veces.
#
# ATENCIÓN: ni + ni * modifican las listas originales.
#   Crean una lista NUEVA. Si quieres conservarla, guárdala en una variable.

print("=== 3. CONCATENAR (+) Y REPETIR (*) ===")

party2 = ['Naruto', 'Luffy']

print(party + party2)   # Salida: ['Link', 'Cloud', 'Goku', 'Naruto', 'Luffy']
print(party * 2)        # Salida: ['Link', 'Cloud', 'Goku', 'Link', 'Cloud', 'Goku']

potions = ['Poción'] * 3     # Tres pociones iguales
print(potions)               # Salida: ['Poción', 'Poción', 'Poción']

big_party = party + party2   # Guardamos el resultado en una variable nueva
print(big_party)             # Salida: ['Link', 'Cloud', 'Goku', 'Naruto', 'Luffy']

print(party)                 # Salida: ['Link', 'Cloud', 'Goku']  (la original NO cambió)
print()


# =====================================================================
# 4. INDEXACIÓN: ACCEDER A UN ELEMENTO
# =====================================================================
# QUÉ ES:
#   El índice es el NÚMERO DE CASILLA de un elemento. Se usa así:
#       nombre_de_la_lista[índice]
#
# REGLA CLAVE: el primer elemento tiene índice 0.
#
# También hay índices NEGATIVOS, que cuentan desde el final:
#       -1 es el último, -2 es el penúltimo, etc.
#
# TABLA de la lista 'heroes' (7 elementos):
#
#   Elemento:    Link  Cloud  Goku  Naruto  Luffy  Zelda  Samus
#   Índice +:      0     1     2      3       4      5      6
#   Índice -:     -7    -6    -5     -4      -3     -2     -1
#
# ATENCIÓN: si usas un índice que no existe, da IndexError.
#   Con 7 elementos, el último índice positivo es 6, no 7.

print("=== 4. INDEXACIÓN ===")

heroes = ['Link', 'Cloud', 'Goku', 'Naruto', 'Luffy', 'Zelda', 'Samus']

print(heroes[0])     # Salida: Link   (el primero)
print(heroes[1])     # Salida: Cloud  (el segundo)
print(heroes[-1])    # Salida: Samus  (el último)
print(heroes[-2])    # Salida: Zelda  (el penúltimo)

# Error a propósito: la casilla 7 no existe (solo hay de la 0 a la 6).
try:
    print(heroes[7])
except IndexError as error:
    print("Error:", error)   # Salida: Error: list index out of range
print()


# =====================================================================
# 5. MODIFICAR UN ELEMENTO
# =====================================================================
# QUÉ ES:
#   Como las listas son mutables, puedes cambiar una casilla
#   asignándole un valor nuevo:
#       lista[índice] = valor_nuevo
#
# ANALOGÍA RPG:
#   Cambiar tu espada de madera por una de acero en la misma casilla.

print("=== 5. MODIFICAR UN ELEMENTO ===")

equipment = ['Espada de madera', 'Escudo de madera', 'Casco de cuero']
print(equipment)         # Salida: ['Espada de madera', 'Escudo de madera', 'Casco de cuero']

equipment[0] = 'Espada de acero'    # Cambiamos la casilla 0
print(equipment)         # Salida: ['Espada de acero', 'Escudo de madera', 'Casco de cuero']

equipment[-1] = 'Casco de hierro'   # Cambiamos la última casilla
print(equipment)         # Salida: ['Espada de acero', 'Escudo de madera', 'Casco de hierro']
print()


# =====================================================================
# 6. SLICING: CORTAR TROZOS DE UNA LISTA
# =====================================================================
# QUÉ ES:
#   Un "slice" (rebanada) te da una SUB-LISTA. Forma general:
#       lista[inicio : fin : paso]
#
#   - inicio: primer índice que se INCLUYE.
#   - fin:    índice donde se PARA. Ese índice NO se incluye.
#   - paso:   de cuánto en cuánto se avanza (por defecto 1).
#
#   Si omites un valor, Python usa uno por defecto:
#       sin inicio -> empieza en el principio
#       sin fin    -> llega hasta el final
#
# REGLA QUE MÁS CONFUNDE: el "fin" NO se incluye.
#   [0:3] significa "desde el índice 0 hasta el 2".
#
# ANALOGÍA RPG:
#   Seleccionar un rango de casillas del inventario con el ratón.
#
# ATENCIÓN: un slice NUNCA da error por pasarte del final.
#   Simplemente te da lo que haya.

print("=== 6. SLICING ===")

# Recordatorio: heroes = ['Link','Cloud','Goku','Naruto','Luffy','Zelda','Samus']

print(heroes[0:3])     # Salida: ['Link', 'Cloud', 'Goku']  (índices 0, 1, 2)
print(heroes[2:])      # Salida: ['Goku', 'Naruto', 'Luffy', 'Zelda', 'Samus']  (del 2 al final)
print(heroes[:4])      # Salida: ['Link', 'Cloud', 'Goku', 'Naruto']  (del principio al 3)
print(heroes[0:6:2])   # Salida: ['Link', 'Goku', 'Luffy']  (índices 0, 2, 4)
print(heroes[::2])     # Salida: ['Link', 'Goku', 'Luffy', 'Samus']  (índices 0, 2, 4, 6)
print(heroes[-3:])     # Salida: ['Luffy', 'Zelda', 'Samus']  (los 3 últimos)

# Truco: paso negativo = recorrer al revés.
print(heroes[::-1])    # Salida: ['Samus', 'Zelda', 'Luffy', 'Naruto', 'Goku', 'Cloud', 'Link']

# Un slice se pasa del final y NO da error:
print(heroes[5:100])   # Salida: ['Zelda', 'Samus']
print()


# =====================================================================
# 7. TAMAÑO Y EXTREMOS: len, min, max, sum
# =====================================================================
# QUÉ ES:
#   - len(lista): cuántos elementos tiene.
#   - min(lista): el "menor" elemento.
#   - max(lista): el "mayor" elemento.
#   - sum(lista): la suma (SOLO si todos son números).
#
# CÓMO SE COMPARAN:
#   - Números: por valor (5 es menor que 10).
#   - Textos: por orden alfabético (la 'A' va antes que la 'Z').
#
# ATENCIÓN: no puedes comparar textos con números en la misma lista
#   (daría TypeError).

print("=== 7. TAMAÑO Y EXTREMOS ===")

print(len(heroes))     # Salida: 7
print(min(heroes))     # Salida: Cloud  (primero por orden alfabético)
print(max(heroes))     # Salida: Zelda  (último por orden alfabético)

damages = [120, 45, 300, 80]   # Daño de cuatro ataques
print(len(damages))    # Salida: 4
print(min(damages))    # Salida: 45
print(max(damages))    # Salida: 300
print(sum(damages))    # Salida: 545   (120 + 45 + 300 + 80)
print()


# =====================================================================
# 8. ORDENAR SIN TOCAR LA ORIGINAL: sorted()
# =====================================================================
# QUÉ ES:
#   sorted(lista) devuelve una lista NUEVA ordenada.
#   La lista original queda igual.
#
#   Para orden de mayor a menor: sorted(lista, reverse=True)

print("=== 8. sorted() ===")

print(sorted(heroes))
# Salida: ['Cloud', 'Goku', 'Link', 'Luffy', 'Naruto', 'Samus', 'Zelda']

print(sorted(damages))                  # Salida: [45, 80, 120, 300]
print(sorted(damages, reverse=True))    # Salida: [300, 120, 80, 45]

print(heroes)
# Salida: ['Link', 'Cloud', 'Goku', 'Naruto', 'Luffy', 'Zelda', 'Samus']
# (la original NO cambió)
print()


# =====================================================================
# 9. BUSCAR: index() Y count()
# =====================================================================
# QUÉ ES:
#   - lista.index(x): devuelve la POSICIÓN de la primera aparición de x.
#   - lista.index(x, desde): empieza a buscar desde ese índice.
#   - lista.index(x, desde, hasta): busca entre dos índices
#                                   (el "hasta" NO se incluye).
#   - lista.count(x): cuántas veces aparece x.
#
# ATENCIÓN: si x no está, index() da ValueError. count() NO da error:
#   devuelve 0.
#
# ANALOGÍA RPG:
#   Mirar el bestiario: "¿en qué casilla está el primer Slime?" y
#   "¿cuántos Slimes hay?".

print("=== 9. index() y count() ===")

monsters = ['Slime', 'Goblin', 'Slime', 'Dragón', 'Slime']
# Índices:     0        1         2        3         4

print(monsters.index('Slime'))         # Salida: 0  (primera aparición)
print(monsters.index('Dragón'))        # Salida: 3
print(monsters.index('Slime', 1))      # Salida: 2  (buscando desde el índice 1)
print(monsters.index('Slime', 3))      # Salida: 4  (buscando desde el índice 3)
print(monsters.index('Slime', 1, 3))   # Salida: 2  (buscando entre los índices 1 y 2)

# Error a propósito: el Dragón está en el índice 3, pero buscamos solo en 0, 1 y 2.
try:
    print(monsters.index('Dragón', 0, 3))
except ValueError as error:
    print("Error:", error)    # Salida: Error: 'Dragón' is not in list

# Error a propósito: un elemento que no existe.
try:
    print(monsters.index('Beholder'))
except ValueError as error:
    print("Error:", error)    # Salida: Error: 'Beholder' is not in list

print(monsters.count('Slime'))      # Salida: 3
print(monsters.count('Goblin'))     # Salida: 1
print(monsters.count('Beholder'))   # Salida: 0  (count() no da error)
print()


# =====================================================================
# 10. AÑADIR: append(), extend(), insert()
# =====================================================================
# QUÉ ES:
#   - append(x):      añade UN elemento al FINAL.
#   - extend(lista):  añade VARIOS elementos al final (de otra lista).
#   - insert(i, x):   mete x en la posición i; los demás se desplazan.
#
# DIFERENCIA CLAVE entre append y extend:
#   - append(['a','b']) mete la lista ENTERA como UN solo elemento.
#   - extend(['a','b']) mete 'a' y 'b' como DOS elementos separados.
#
# ATENCIÓN con insert(-1, x):
#   NO añade al final. Inserta ANTES del último elemento.
#   Para añadir al final, usa append().
#
# ANALOGÍA RPG:
#   Recoger botín tras un combate: un objeto suelto (append), un cofre
#   entero (extend) o meter un objeto en una casilla concreta (insert).
#
# NOTA: estos métodos MODIFICAN la lista original y no devuelven nada.

print("=== 10. append(), extend(), insert() ===")

loot = ['Oro']
print(loot)                         # Salida: ['Oro']

loot.append('Gema')                 # Un objeto al final
print(loot)                         # Salida: ['Oro', 'Gema']

loot.extend(['Poción', 'Mapa'])     # Varios objetos al final
print(loot)                         # Salida: ['Oro', 'Gema', 'Poción', 'Mapa']

# Comparación: append con una lista dentro
loot_wrong = ['Oro']
loot_wrong.append(['Poción', 'Mapa'])
print(loot_wrong)                   # Salida: ['Oro', ['Poción', 'Mapa']]
# Se ha creado una lista DENTRO de la lista (sección 15). Dos objetos, no tres.

loot.insert(1, 'Llave')             # En la casilla 1; el resto se desplaza
print(loot)                         # Salida: ['Oro', 'Llave', 'Gema', 'Poción', 'Mapa']

loot.insert(-1, 'Brújula')          # ANTES del último elemento
print(loot)                         # Salida: ['Oro', 'Llave', 'Gema', 'Poción', 'Brújula', 'Mapa']
print()


# =====================================================================
# 11. ELIMINAR: remove(), del, pop(), clear()
# =====================================================================
# QUÉ ES:
#   - remove(x):  elimina la PRIMERA aparición del VALOR x.
#   - del lista[i]: elimina el elemento en la POSICIÓN i.
#   - pop(i):     elimina el elemento en la posición i Y TE LO DEVUELVE.
#                 Sin número, elimina el último.
#   - clear():    vacía toda la lista.
#
# DIFERENCIA CLAVE:
#   - remove() trabaja con el VALOR   ("quita la Poción").
#   - del y pop() trabajan con el ÍNDICE ("quita lo que hay en la casilla 1").
#
# ATENCIÓN:
#   - pop() necesita un NÚMERO (índice), nunca un texto.
#     pop('Antorcha') da TypeError. Para borrar por valor, usa remove().
#   - remove() con un valor inexistente da ValueError.
#
# ANALOGÍA RPG:
#   - remove: "tirar la primera Poción que encuentres".
#   - del:    "tirar lo que hay en la casilla 1".
#   - pop:    "sacar un objeto de la casilla y quedártelo en la mano".
#   - clear:  "vaciar la mochila entera".

print("=== 11. ELIMINAR ===")

backpack = ['Poción', 'Espada', 'Poción', 'Mapa', 'Antorcha', 'Llave']
# Índices:     0         1         2        3         4          5

backpack.remove('Poción')           # Quita solo la PRIMERA 'Poción'
print(backpack)                     # Salida: ['Espada', 'Poción', 'Mapa', 'Antorcha', 'Llave']

try:
    backpack.remove('Dragón')       # No existe en la lista
except ValueError as error:
    print("Error:", error)          # Salida: Error: list.remove(x): x not in list
    # (el texto exacto puede variar un poco según tu versión de Python)

del backpack[1]                     # Borra lo que hay en la casilla 1 (la 'Poción')
print(backpack)                     # Salida: ['Espada', 'Mapa', 'Antorcha', 'Llave']

last = backpack.pop()               # Saca el ÚLTIMO y lo guarda en 'last'
print(last)                         # Salida: Llave
print(backpack)                     # Salida: ['Espada', 'Mapa', 'Antorcha']

second = backpack.pop(1)            # Saca el de la casilla 1
print(second)                       # Salida: Mapa
print(backpack)                     # Salida: ['Espada', 'Antorcha']

# Error a propósito: pop() NO acepta texto.
try:
    backpack.pop('Antorcha')
except TypeError as error:
    print("Error:", error)          # Salida: Error: 'str' object cannot be interpreted as an integer

backpack.remove('Antorcha')         # Esta es la forma correcta de borrar por valor
print(backpack)                     # Salida: ['Espada']

backpack.clear()                    # Vacía la mochila
print(backpack)                     # Salida: []
print()


# =====================================================================
# 12. reverse() Y sort()
# =====================================================================
# QUÉ ES:
#   - reverse(): da la vuelta a la lista (el último pasa a ser el primero).
#   - sort():    ordena la lista (alfabético o de menor a mayor).
#   - sort(reverse=True): ordena de mayor a menor.
#
# DIFERENCIA CON sorted() (sección 8):
#   - sorted(lista) -> crea una lista NUEVA. La original no cambia.
#   - lista.sort()  -> CAMBIA la lista original.
#
# ATENCIÓN (error muy común):
#   lista.sort() y lista.reverse() devuelven None (nada).
#   NO escribas:  lista = lista.sort()
#   Eso dejaría tu lista convertida en None.

print("=== 12. reverse() y sort() ===")

turn_order = ['Zelda', 'Link', 'Samus', 'Cloud']
print(turn_order)       # Salida: ['Zelda', 'Link', 'Samus', 'Cloud']

turn_order.reverse()
print(turn_order)       # Salida: ['Cloud', 'Samus', 'Link', 'Zelda']

turn_order.sort()
print(turn_order)       # Salida: ['Cloud', 'Link', 'Samus', 'Zelda']

turn_order.sort(reverse=True)
print(turn_order)       # Salida: ['Zelda', 'Samus', 'Link', 'Cloud']

levels = [42, 7, 99, 15]
levels.sort()
print(levels)           # Salida: [7, 15, 42, 99]

# La trampa del None:
levels2 = [42, 7, 99, 15]
result = levels2.sort()     # sort() modifica levels2 pero NO devuelve nada
print(result)               # Salida: None
print(levels2)              # Salida: [7, 15, 42, 99]
print()


# =====================================================================
# 13. COPIAR LISTAS: copy(), list() Y LA TRAMPA DEL "ALIAS"
# =====================================================================
# QUÉ ES:
#   Si haces  b = a  NO copias la lista. Solo creas un segundo NOMBRE
#   para la MISMA lista (un "alias").
#
# ANALOGÍA RPG:
#   Dos mandos de control para el mismo personaje: lo que hagas con uno
#   se ve en el otro. NO es un clon.
#
# Para hacer una copia independiente (un clon real):
#   - lista.copy()
#   - list(lista)
#   - lista[:]   (un slice completo)
#
# NOTA AVANZADA (para más adelante): estas copias son "superficiales".
#   Si la lista contiene listas dentro, esas listas internas se siguen
#   compartiendo. No hace falta que lo domines ahora.

print("=== 13. COPIAR LISTAS ===")

hero_team = ['Link', 'Cloud']

alias = hero_team            # NO es una copia: es el mismo grupo con otro nombre
alias.append('Goku')
print(alias)                 # Salida: ['Link', 'Cloud', 'Goku']
print(hero_team)             # Salida: ['Link', 'Cloud', 'Goku']  (¡también cambió!)

backup = hero_team.copy()    # Copia REAL e independiente
backup.append('Zelda')
print(backup)                # Salida: ['Link', 'Cloud', 'Goku', 'Zelda']
print(hero_team)             # Salida: ['Link', 'Cloud', 'Goku']  (la original NO cambió)

new_team = list(hero_team)   # Otra forma de copiar
print(new_team)              # Salida: ['Link', 'Cloud', 'Goku']

slice_copy = hero_team[:]    # Otra forma más: un slice completo
print(slice_copy)            # Salida: ['Link', 'Cloud', 'Goku']
print()


# =====================================================================
# 14. COMPARAR LISTAS: == FRENTE A is
# =====================================================================
# QUÉ ES:
#   - ==  pregunta: "¿tienen el MISMO CONTENIDO?"
#   - is  pregunta: "¿son EXACTAMENTE el MISMO OBJETO en la memoria?"
#
# ANALOGÍA RPG:
#   Dos espadas idénticas en la tienda:
#   - == es "¿son del mismo tipo y con las mismas estadísticas?" -> Sí.
#   - is es "¿son literalmente la misma espada física?" -> No.
#
# Dos listas con el mismo contenido son == pero NO son "is".
# Un alias (sección 13) sí es "is".

print("=== 14. == frente a is ===")

team_a = ['Link', 'Cloud']
team_b = ['Link', 'Cloud']

print(team_a == team_b)          # Salida: True   (mismo contenido)
print(team_a is team_b)          # Salida: False  (son dos objetos distintos)

team_c = team_a                  # Alias: mismo objeto con otro nombre
print(team_c is team_a)          # Salida: True

# El ORDEN importa al comparar:
print(['Link', 'Cloud'] == ['Cloud', 'Link'])   # Salida: False
print()


# =====================================================================
# 15. LISTAS ANIDADAS (LISTAS DENTRO DE LISTAS)
# =====================================================================
# QUÉ ES:
#   Un elemento de una lista puede ser otra lista. Para llegar al
#   elemento interno se usan DOS índices seguidos:
#       lista[índice_exterior][índice_interior]
#
# ANALOGÍA RPG:
#   Un mapa del mundo dividido en regiones. Cada región es una lista
#   de lugares. Primero eliges la región y luego el lugar.
#
#   world_map[0] -> región 0 (Llanura)
#   world_map[0][1] -> lugar 1 de la región 0

print("=== 15. LISTAS ANIDADAS ===")

world_map = [
    ['Aldea', 'Bosque'],              # Región 0
    ['Castillo', 'Mazmorra'],         # Región 1
    ['Volcán', 'Nube', 'Luna'],       # Región 2
]

print(world_map[0])          # Salida: ['Aldea', 'Bosque']
print(world_map[1][0])       # Salida: Castillo  (región 1, lugar 0)
print(world_map[2][-1])      # Salida: Luna      (región 2, último lugar)
print(len(world_map))        # Salida: 3  (hay 3 regiones)
print(len(world_map[2]))     # Salida: 3  (la región 2 tiene 3 lugares)

world_map[0][1] = 'Bosque Maldito'   # Modificar un lugar concreto
print(world_map[0])          # Salida: ['Aldea', 'Bosque Maldito']
print()


# =====================================================================
# 16. DESEMPAQUETADO
# =====================================================================
# QUÉ ES:
#   Repartir los elementos de una lista en VARIAS variables en una
#   sola línea.
#
# REGLA: el número de variables debe coincidir con el número de
#   elementos. Si no, da ValueError.
#
# ESTRELLA (*): una variable con * recoge "todo lo que sobre" y lo
#   guarda SIEMPRE como lista. Solo puede haber una variable con *.
#
# ANALOGÍA RPG:
#   Asignar roles al formar el grupo: el primero es el líder, el
#   segundo el sanador, el tercero el tanque.

print("=== 16. DESEMPAQUETADO ===")

squad = ['Link', 'Cloud', 'Goku']

leader, healer, tank = squad
print(leader)     # Salida: Link
print(healer)     # Salida: Cloud
print(tank)       # Salida: Goku

# Error a propósito: 2 variables para 3 elementos.
try:
    a, b = squad
except ValueError as error:
    print("Error:", error)    # Salida: Error: too many values to unpack (expected 2)

# Con estrella: el primero a una variable y "el resto" a una lista.
first, *others = squad
print(first)      # Salida: Link
print(others)     # Salida: ['Cloud', 'Goku']

# La estrella también puede ir en medio:
captain, *crew, mascot = heroes
print(captain)    # Salida: Link
print(crew)       # Salida: ['Cloud', 'Goku', 'Naruto', 'Luffy', 'Zelda']
print(mascot)     # Salida: Samus
print()


# =====================================================================
# 17. CREAR LISTAS CON list() Y range()
# =====================================================================
# QUÉ ES:
#   - list(algo) convierte "algo que se puede recorrer" en una lista.
#   - range(n) genera los números desde 0 hasta n-1 (n NO se incluye).
#   - range(inicio, fin) y range(inicio, fin, paso) funcionan como
#     los slices de la sección 6.
#   - Un texto se convierte en una lista de LETRAS.
#
# ATENCIÓN: print(range(5)) NO muestra los números. Hay que envolverlo
#   con list() para verlos.

print("=== 17. list() Y range() ===")

print(list(range(5)))          # Salida: [0, 1, 2, 3, 4]
print(list(range(1, 6)))       # Salida: [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))   # Salida: [0, 2, 4, 6, 8]

print(list('Zelda'))           # Salida: ['Z', 'e', 'l', 'd', 'a']

print(list())                  # Salida: []  (otra forma de crear una lista vacía)
print()


# =====================================================================
# 18. RESUMEN FINAL Y RETO
# =====================================================================
# RESUMEN RÁPIDO (cada fila: qué quiero hacer -> cómo se hace)
#
#  Quiero...                          Uso...
#  --------------------------------   ------------------------------
#  Saber si algo está                 x in lista  /  x not in lista
#  Unir dos listas                    lista1 + lista2
#  Repetir una lista                  lista * n
#  Ver un elemento                    lista[i]
#  Cambiar un elemento                lista[i] = nuevo
#  Cortar un trozo                    lista[inicio:fin:paso]
#  Saber cuántos hay                  len(lista)
#  Menor / mayor / suma               min(lista) / max(lista) / sum(lista)
#  Lista nueva ordenada               sorted(lista)
#  Ordenar la propia lista            lista.sort()
#  Dar la vuelta                      lista.reverse()
#  Posición de un valor               lista.index(x)
#  Contar apariciones                 lista.count(x)
#  Añadir uno al final                lista.append(x)
#  Añadir varios al final             lista.extend([...])
#  Añadir en una posición             lista.insert(i, x)
#  Quitar por valor                   lista.remove(x)
#  Quitar por posición                del lista[i]  /  lista.pop(i)
#  Vaciar                             lista.clear()
#  Copia independiente                lista.copy()  /  list(lista)
#
# ERRORES MÁS COMUNES (revisa esta lista si algo falla):
#   1. Contar desde 1 en vez de desde 0.
#   2. Olvidar que en un slice el "fin" NO se incluye.
#   3. Usar pop('texto'): pop necesita un NÚMERO. Para texto, remove().
#   4. Escribir  lista = lista.sort()  (deja la lista en None).
#   5. Creer que  b = a  hace una copia (es un alias).
#   6. Confundir append (uno) con extend (varios).
#   7. Pensar que insert(-1, x) añade al final (inserta ANTES del último).

print("=== 18. RETO FINAL ===")

# RETO (hazlo tú, escribiendo código debajo de cada punto):
#   1. Crea una lista llamada 'inventory' con 4 objetos de tu RPG favorito.
#   2. Añade un objeto nuevo al final.
#   3. Inserta una 'Poción' en la posición 0.
#   4. Elimina el segundo objeto usando pop().
#   5. Imprime los dos últimos objetos usando un slice.
#   6. Crea una copia llamada 'backup' e imprime si inventory == backup
#      y si inventory is backup. ¿Qué esperas que salga?
#
# Escribe tu solución aquí abajo:

print("¡Fin de la guía de listas! Has completado la mazmorra.")
