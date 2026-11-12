# =============================================================================
# COMENTARIOS DE TEXTO
# Ejercicios de Programación estructurada — Programación (DAW)
# Ricardo Pérez López — IES Doñana — Curso 2026/2027
#
# Para cada enunciado se incluye: el enunciado, un comentario de texto
# (análisis de qué se pide, conceptos que evalúa y plan de resolución)
# y un esqueleto de resolución en Python.
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1
# Enunciado: Explicar la diferencia entre el operador ternario
#     <expresión1> if <condición> else <expresión2>
# y la estructura de control
#     if <condición>: <sentencia1>  else: <sentencia2>
#
# COMENTARIO DE TEXTO:
# La diferencia fundamental es que el operador ternario es una EXPRESIÓN:
# produce un valor y puede aparecer en cualquier lugar donde se espere una
# expresión (lado derecho de una asignación, argumento de una función,
# valor de retorno, etc.). La estructura if/else, en cambio, es una
# SENTENCIA (estructura de control alternativa): no produce un valor, sino
# que ejecuta un bloque u otro de sentencias según la condición.
# Por eso el ternario solo admite expresiones en sus ramas, mientras que
# la estructura admite bloques completos de sentencias.
#
# Plan: mostrar ambos con el mismo ejemplo (mayoría de edad) y señalar
# que el ternario equivale a la estructura cuando las ramas son una sola
# sentencia de asignación.
# -----------------------------------------------------------------------------


def ejercicio_1() -> None:
    # Operador ternario: es una expresión que devuelve un valor.
    edad: int = 30
    mensaje: str = 'Qué joven!' if edad < 25 else 'Qué mayor!'
    print(mensaje)

    # Estructura de control: es una sentencia que ejecuta un bloque.
    if edad < 25:
        mensaje = 'Qué joven!'
    else:
        mensaje = 'Qué mayor!'
    print(mensaje)


# -----------------------------------------------------------------------------
# EJERCICIO 2
# Enunciado: Escribir un programa que pida al usuario su edad y que imprima
# el mensaje «¡Qué joven!» si es menor de 25 años.
#
# COMENTARIO DE TEXTO:
# Ejercicio de introducción a la estructura alternativa SIMPLE (if sin else).
# Se pide: (1) entrada de datos por teclado (input) con conversión a entero,
# (2) una condición de comparación (edad < 25) y (3) una salida condicionada.
# Punto clave: si la condición es falsa, el programa simplemente no imprime
# nada; no hay rama alternativa.
#
# Plan: leer la edad con int(input(...)) y usar un if simple.
# -----------------------------------------------------------------------------


def ejercicio_2() -> None:
    edad: int = int(input('¿Cuántos años tienes?: '))
    if edad < 25:
        print('¡Qué joven!')


# -----------------------------------------------------------------------------
# EJERCICIO 3
# Enunciado: Igual que el 2, pero imprimiendo «¡Qué mayor!» en caso contrario.
#
# COMENTARIO DE TEXTO:
# Evolución natural del ejercicio anterior: ahora la estructura alternativa
# es COMPLETA (if/else). Introduce el concepto de rama alternativa y obliga
# a razonar que «en caso contrario» cubre exactamente el complementario de
# la condición (edad >= 25). Los dos mensajes son excluyentes y exhaustivos.
#
# Plan: if/else con la misma condición; el else recoge el caso contrario.
# -----------------------------------------------------------------------------


def ejercicio_3() -> None:
    edad: int = int(input('¿Cuántos años tienes?: '))
    if edad < 25:
        print('¡Qué joven!')
    else:
        print('¡Qué mayor!')


# -----------------------------------------------------------------------------
# EJERCICIO 4
# Enunciado: Igual que el 3, pero con «No está mal.» si tiene entre 25 y 40
# años (y nada si tiene más de 40).
#
# COMENTARIO DE TEXTO:
# Aparece una condición COMPUESTA con dos límites: 25 <= edad <= 40.
# Python permite encadenar comparaciones (25 <= edad <= 40), forma idiomática
# que conviene destacar. La estructura deja de ser binaria: hay tres tramos
# pero solo dos generan salida, por lo que se usa if/elif/else... o mejor,
# if/elif/else donde el último else no imprime nada, o simplemente dos if
# excluyentes. La solución limpia es if/elif con else vacío o sin else final.
#
# Plan: if edad < 25 ... elif edad <= 40 ... (y nada más).
# -----------------------------------------------------------------------------


def ejercicio_4() -> None:
    edad: int = int(input('¿Cuántos años tienes?: '))
    if edad < 25:
        print('¡Qué joven!')
    elif edad <= 40:
        print('No está mal.')
    # Si tiene más de 40 años, no se imprime nada.


# -----------------------------------------------------------------------------
# EJERCICIO 5
# Enunciado: Igual que el 4, pero añadiendo «¡Qué mayor!» si tiene más de
# 40 años.
#
# COMENTARIO DE TEXTO:
# Es el caso general de la alternativa MÚLTIPLE: tres tramos disjuntos que
# cubren todos los casos (menor de 25, entre 25 y 40, mayor de 40). Se
# evalúa la estructura if/elif/else completa. Concepto importante: en una
# cadena if/elif/else las condiciones se comprueban en orden y solo se
# ejecuta la primera rama verdadera, por lo que no hace falta escribir
# 25 <= edad <= 40 en el elif: basta edad <= 40.
#
# Plan: if/elif/else con tres ramas.
# -----------------------------------------------------------------------------


def ejercicio_5() -> None:
    edad: int = int(input('¿Cuántos años tienes?: '))
    if edad < 25:
        print('¡Qué joven!')
    elif edad <= 40:
        print('No está mal.')
    else:
        print('¡Qué mayor!')


# -----------------------------------------------------------------------------
# EJERCICIO 6
# Enunciado: Escribir un programa que muestre por pantalla la tabla de
# multiplicar de un número comprendido entre 0 y 10, introducido por teclado.
#
# COMENTARIO DE TEXTO:
# Primer ejercicio con estructura repetitiva (bucle). Requiere: (1) entrada
# con VALIDACIÓN (el número debe estar entre 0 y 10; si no, se avisa o se
# vuelve a pedir), (2) un bucle que recorra los factores 0..10 y (3) salida
# formateada de cada línea de la tabla. Evalúa el bucle for con range() y la
# validación de rangos.
#
# Plan: validar la entrada con un bucle while, y luego un for i in range(11)
# que imprime n x i = n*i.
# -----------------------------------------------------------------------------


def ejercicio_6() -> None:
    n: int = int(input('Número entre 0 y 10: '))
    while n < 0 or n > 10:
        print('Error: debe estar entre 0 y 10.')
        n = int(input('Número entre 0 y 10: '))
    for i in range(11):
        print(f'{n} x {i} = {n * i}')


# -----------------------------------------------------------------------------
# EJERCICIO 7
# Enunciado: Dado el código
#     n = int(input('¿Hasta dónde llego?: '))
#     i = 0
#     while i < n:
#         print('Aquí la i vale', i)
#         i += 2
# se pide:
#   a) Describir con una sola frase, sin términos técnicos, qué hace.
#   b) Contar cuántas sentencias hay.
#   c) Indicar si son simples o compuestas.
#   d) Indicar el tipo de estructura de cada sentencia compuesta.
#   e) Deducir cuántas veces se ejecuta la línea 4 en función de n.
#   f) ¿Es posible provocar un bucle infinito?
#
# COMENTARIO DE TEXTO (respuestas):
# a) «El programa va contando de dos en dos desde cero hasta acercarse al
#    número que le digas, mostrando por dónde va.»
# b) Hay 2 sentencias simples (las líneas 1 y 2) y 1 sentencia compuesta
#    (el while de la línea 3, que contiene otras 2 sentencias simples en su
#    cuerpo). En total, 5 sentencias si se cuentan las anidadas; 3 si se
#    cuentan las de primer nivel.
# c) Las líneas 1, 2, 4 y 5 son simples; la línea 3 (while) es compuesta.
# d) La única compuesta es una estructura repetitiva (bucle while, con
#    condición previa).
# e) La línea 4 se ejecuta una vez por cada valor de i en 0, 2, 4, ...,
#    es decir, ceil(n/2) veces si n > 0; ninguna vez si n <= 0. En general:
#    (n + 1) // 2 veces para n >= 0.
# f) No: i += 2 hace crecer i indefinidamente, así que la condición i < n
#    acabará siendo falsa para cualquier n entero (aunque n sea negativo,
#    el bucle no llega a ejecutarse). No hay bucle infinito posible.
# -----------------------------------------------------------------------------


def ejercicio_7() -> None:
    n: int = int(input('¿Hasta dónde llego?: '))
    i: int = 0
    while i < n:
        print('Aquí la i vale', i)
        i += 2


# -----------------------------------------------------------------------------
# EJERCICIO 8
# Enunciado: Escribir un programa que calcule la media de cinco valores
# numéricos reales (tipo float) introducidos por teclado.
#
# COMENTARIO DE TEXTO:
# Ejercicio clásico de ACUMULACIÓN. Evalúa: (1) lectura repetida de datos
# (bucle fijo: exactamente 5 iteraciones, luego for in range(5)), (2)
# conversión a float y (3) un acumulador (suma) que se inicializa a 0 antes
# del bucle y se divide por el número de valores al final. Concepto clave:
# la diferencia entre contador y acumulador.
#
# Plan: acumular la suma en un bucle for de 5 iteraciones y dividir por 5.
# -----------------------------------------------------------------------------


def ejercicio_8() -> None:
    suma: float = 0.0
    for i in range(5):
        suma += float(input(f'Valor {i + 1}: '))
    print(f'La media es {suma / 5}')


# -----------------------------------------------------------------------------
# EJERCICIO 9
# Enunciado: Escribir un programa que guarde en una lista diez cadenas
# introducidas por teclado y luego las muestre en orden inverso a como se
# han introducido, desde la última hasta la primera.
# Indicación: usar append y luego un bucle que recorra la lista desde el
# último elemento hasta el primero.
#
# COMENTARIO DE TEXTO:
# Introduce el tipo lista y el método append (construcción incremental de
# una colección). El recorrido inverso pedido (desde el último hasta el
# primero) se resuelve idiomáticamente con range(len(lista) - 1, -1, -1) o,
# de forma más pitónica, con reversed(lista) o lista[::-1]; la indicación
# sugiere el primero para practicar el control de índices. Evalúa listas,
# índices negativos/rangos descendentes y bucles sobre colecciones.
#
# Plan: for de 10 lecturas con append; luego recorrido inverso con range
# descendente (y comentario de las alternativas reversed y slicing).
# -----------------------------------------------------------------------------


def ejercicio_9() -> None:
    cadenas: list[str] = []
    for i in range(10):
        cadenas.append(input(f'Cadena {i + 1}: '))
    for i in range(len(cadenas) - 1, -1, -1):
        print(cadenas[i])
    # Alternativas más pitónicas:
    #   for cadena in reversed(cadenas): print(cadena)
    #   for cadena in cadenas[::-1]: print(cadena)


# -----------------------------------------------------------------------------
# EJERCICIO 10
# Enunciado: Escribir un programa que calcule el máximo común divisor de dos
# números enteros introducidos por teclado, usando:
#   a) La función math.gcd.
#   b) Bucles.
#
# COMENTARIO DE TEXTO:
# Contraste entre solución de biblioteca y solución algorítmica. La parte a)
# es trivial (import math; math.gcd(a, b)) y sirve para conocer la librería
# estándar. La parte b) pide implementar el algoritmo de EUCLIDES con un
# bucle: mientras b != 0, se sustituye (a, b) por (b, a % b); al terminar, a
# es el mcd. Evalúa importación de módulos, bucles con condición de salida
# y asignación múltiple/tuplas.
#
# Plan: dos funciones, una con math.gcd y otra con el algoritmo de Euclides.
# -----------------------------------------------------------------------------


import math


def mcd_bucles(a: int, b: int) -> int:
    # Algoritmo de Euclides.
    while b != 0:
        a, b = b, a % b
    return abs(a)


def ejercicio_10() -> None:
    a: int = int(input('Primer número: '))
    b: int = int(input('Segundo número: '))
    print(f'MCD con math.gcd: {math.gcd(a, b)}')
    print(f'MCD con bucles:   {mcd_bucles(a, b)}')


# -----------------------------------------------------------------------------
# EJERCICIO 11
# Enunciado: Escribir un programa que determine si un número entero
# introducido por teclado es primo o compuesto.
# Indicación: un número primo sólo puede dividirse exactamente por sí mismo
# y por 1.
#
# COMENTARIO DE TEXTO:
# Ejercicio de lógica con bucle y bandera (flag). Puntos a tratar: (1) los
# casos especiales (n < 2 no es primo: 0, 1 y los negativos son compuestos
# o no primos), (2) buscar un divisor con un bucle desde 2, pudiendo parar
# en la raíz cuadrada de n por eficiencia, y (3) el uso de break para
# abandonar el bucle al encontrar un divisor, o for/else de Python. Evalúa
# bucles con salida anticipada y razonamiento matemático básico.
#
# Plan: recorrer posibles divisores de 2 a sqrt(n); si alguno divide
# exactamente, es compuesto; si no, es primo.
# -----------------------------------------------------------------------------


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(math.isqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def ejercicio_11() -> None:
    n: int = int(input('Número entero: '))
    if es_primo(n):
        print(f'{n} es primo.')
    else:
        print(f'{n} es compuesto.')


# -----------------------------------------------------------------------------
# EJERCICIO 12
# Enunciado: Escribir un programa que gestione datos almacenados en una
# lista, mostrando un menú con las opciones: 1) Añadir un elemento, 2)
# Cambiar el valor de un elemento, 3) Eliminar un elemento, 4) Eliminar
# todos los elementos, 5) Mostrar los elementos, 0) Salir. El programa
# deberá pedir la información necesaria para cada opción elegida.
#
# COMENTARIO DE TEXTO:
# Ejercicio integrador: bucle principal de MENÚ (while con condición de
# salida), selección múltiple (if/elif/else o match/case) y operaciones
# básicas sobre listas (append, asignación por índice, del/pop/remove,
# clear, recorrido). Conceptos clave: estructura de programa dirigido por
# menú, validación de índices (evitar IndexError) y actualización de la
# condición del bucle dentro del cuerpo.
#
# Plan: while infinito que muestra el menú, lee la opción y ejecuta la
# operación correspondiente; la opción 0 rompe el bucle.
# -----------------------------------------------------------------------------


def ejercicio_12() -> None:
    lista: list[str] = []
    while True:
        print('\n1. Añadir un elemento a la lista.')
        print('2. Cambiar el valor de un elemento de la lista.')
        print('3. Eliminar un elemento de la lista.')
        print('4. Eliminar todos los elementos de la lista.')
        print('5. Mostrar los elementos de la lista.')
        print('0. Salir del programa.')
        opcion: int = int(input('Opción: '))
        if opcion == 0:
            break
        elif opcion == 1:
            lista.append(input('Nuevo elemento: '))
        elif opcion == 2:
            i = int(input(f'Índice del elemento (0 a {len(lista) - 1}): '))
            if 0 <= i < len(lista):
                lista[i] = input('Nuevo valor: ')
            else:
                print('Índice fuera de rango.')
        elif opcion == 3:
            i = int(input(f'Índice del elemento (0 a {len(lista) - 1}): '))
            if 0 <= i < len(lista):
                del lista[i]
            else:
                print('Índice fuera de rango.')
        elif opcion == 4:
            lista.clear()
        elif opcion == 5:
            print(lista)
        else:
            print('Opción no válida.')


# -----------------------------------------------------------------------------
# EJERCICIO 13
# Enunciado: Los datos de los empleados se almacenan en una lista de tuplas
# (nombre, apellidos, salario). Con la lista dada de cuatro empleados,
# escribir un programa que modifique la lista incrementando en un 10 % el
# salario de cada empleado y muestre por pantalla el salario total de los
# empleados de la empresa.
#
# COMENTARIO DE TEXTO:
# Evalúa listas de tuplas y MODIFICACIÓN IN SITU de estructuras compuestas.
# Punto delicado: las tuplas son inmutables, así que "modificar la lista"
# significa reemplazar cada tupla por una nueva (empleados[i] = (...)) o
# reconstruir la lista. Además se practica el acumulador de suma sobre un
# campo de las tuplas. El incremento del 10 % es salario * 1.10.
#
# Plan: recorrer la lista por índices, crear la tupla modificada y
# acumular el salario total; mostrar el total al final.
# -----------------------------------------------------------------------------


def ejercicio_13() -> None:
    empleados: list[tuple[str, str, float]] = [
        ('María', 'González', 1800.23),
        ('Javier', 'Ruiz', 1630.50),
        ('Jesús', 'Pérez', 2100.42),
        ('Rosa', 'Muñoz', 2240.78),
    ]
    total: float = 0.0
    for i in range(len(empleados)):
        nombre, apellidos, salario = empleados [i]
        incremento: float= salario * 0.10
        nuevo_salario:float = salario + incremento

        empleados[i]= (nombre, apellidos, nuevo_salario)
        total += nuevo_salario

        print(f'{nombre} {apellidos}: +{incremento:.2f} € (Nuevo salario: {nuevo_salario:.2f} €)')
    print(f'\nSalario total de la empresa: {total:.2f}')


# -----------------------------------------------------------------------------
# EJERCICIO 14
# Enunciado: Convertir una cantidad de tiempo en segundos (entero) en la
# correspondiente en horas, minutos y segundos, con el formato:
#     3817 segundos = 1 horas, 3 minutos y 37 segundos
#
# COMENTARIO DE TEXTO:
# Ejercicio de aritmética entera con los operadores de división entera (//)
# y resto (%). La conversión se hace en cascada: horas = s // 3600; el resto
# se descompone en minutos = (s % 3600) // 60 y segundos = s % 60. Evalúa el
# dominio de // y % y la salida formateada con f-strings.
#
# Plan: aplicar las tres fórmulas y presentar el resultado con el formato
# pedido.
# -----------------------------------------------------------------------------


def ejercicio_14() -> None:
    s: int = int(input('Cantidad de segundos: '))
    horas: int = s // 3600
    minutos: int = (s % 3600) // 60
    segundos: int = s % 60
    print(f'{s} segundos = {horas} horas, {minutos} minutos y '
          f'{segundos} segundos')


# -----------------------------------------------------------------------------
# EJERCICIO 15
# Enunciado: Leer los coeficientes a2, a1 y a0 de un polinomio de segundo
# grado a2·x² + a1·x + a0, escribir ese polinomio; después leer el valor de
# x y escribir el valor que toma el polinomio para esa x. Se suponen
# enteros. Ejemplo: coeficientes 1, 2, 3 y x = 2 dan la salida
#     1x^2 + 2x + 3
#     p(2) = 9
#
# COMENTARIO DE TEXTO:
# Combina entrada/salida formateada con la EVALUACIÓN de una expresión
# polinómica. La forma idiomática de evaluar un polinomio es el esquema de
# Horner: ((a2 * x) + a1) * x + a0, aunque también vale la forma directa
# a2 * x ** 2 + a1 * x + a0. Evalúa operadores aritméticos, precedencia y
# f-strings con el formato exacto del ejemplo.
#
# Plan: leer los tres coeficientes, imprimir el polinomio, leer x e
# imprimir p(x) usando Horner.
# -----------------------------------------------------------------------------


def ejercicio_15() -> None:
    a2: int = int(input('Coeficiente a2: '))
    a1: int = int(input('Coeficiente a1: '))
    a0: int = int(input('Coeficiente a0: '))
    print(f'{a2}x^2 + {a1}x + {a0}')
    x: int = int(input('Valor de x: '))
    print(f'p({x}) = {(a2 * x + a1) * x + a0}')


# -----------------------------------------------------------------------------
# EJERCICIO 16
# Enunciado: Escribir un programa apropiado para cada tarea:
#   a. Pedir los dos términos de una fracción y dar el valor de la división,
#      salvo que el denominador sea nulo, en cuyo caso se avisará del error.
#   b. Pedir los coeficientes de una ecuación de segundo grado y dar las dos
#      soluciones, comprobando si el discriminante es positivo o no.
#   c. Pedir los coeficientes de la recta ax + by + c = 0 y dar su pendiente
#      y su ordenada en el origen en caso de que existan, o el mensaje
#      apropiado en otro caso.
#   d. Pedir un número natural n y dar sus divisores.
#
# COMENTARIO DE TEXTO:
# Colección de cuatro miniejercicios que evalúan el CONTROL DE ERRORES con
# alternativas:
# a) División: comprobar denominador != 0 antes de dividir (if/else).
# b) Ecuación de segundo grado: calcular el discriminante d = b² - 4ac y
#    distinguir tres casos: d > 0 (dos soluciones reales), d = 0 (una
#    solución doble) y d < 0 (no hay soluciones reales). Si a = 0 no es de
#    segundo grado.
# c) Recta: la pendiente -a/b solo existe si b != 0; la ordenada en el
#    origen -c/b también requiere b != 0. Casos especiales: b = 0 (recta
#    vertical, sin pendiente ni ordenada) y a = b = 0.
# d) Divisores: bucle for de 1 a n que comprueba n % i == 0. Versión
#    eficiente: recorrer hasta sqrt(n) y añadir los divisores por pares.
#
# Plan: una función por apartado, cada una con su validación previa.
# -----------------------------------------------------------------------------


def ejercicio_16a() -> None:
    numerador: float = float(input('Numerador: '))
    denominador: float = float(input('Denominador: '))
    if denominador != 0:
        print(f'El valor de la división es {numerador / denominador}')
    else:
        print('Error: el denominador no puede ser nulo.')


def ejercicio_16b() -> None:
    a: float = float(input('Coeficiente a: '))
    b: float = float(input('Coeficiente b: '))
    c: float = float(input('Coeficiente c: '))
    if a == 0:
        print('No es una ecuación de segundo grado.')
        return
    discriminante: float = b ** 2 - 4 * a * c
    if discriminante > 0:
        raiz: float = math.sqrt(discriminante)
        print(f'x1 = {(-b + raiz) / (2 * a)}')
        print(f'x2 = {(-b - raiz) / (2 * a)}')
    elif discriminante == 0:
        print(f'Solución doble: x = {-b / (2 * a)}')
    else:
        print('El discriminante es negativo: no hay soluciones reales.')


def ejercicio_16c() -> None:
    a: float = float(input('Coeficiente a: '))
    b: float = float(input('Coeficiente b: '))
    c: float = float(input('Coeficiente c: '))
    if b == 0:
        if a == 0:
            print('No es una recta (0 = 0).' if c == 0
                  else 'No es una recta (ecuación imposible).')
        else:
            print('Recta vertical: no tiene pendiente ni ordenada en el '
                  'origen.')
    else:
        print(f'Pendiente: {-a / b}')
        print(f'Ordenada en el origen: {-c / b}')


def ejercicio_16d() -> None:
    n: int = int(input('Número natural: '))
    if n < 1:
        print('Error: debe ser un número natural (>= 1).')
        return
    divisores: list[int] = [i for i in range(1, n + 1) if n % i == 0]
    print(f'Divisores de {n}: {divisores}')


# -----------------------------------------------------------------------------
# EJERCICIO 17
# Enunciado: Escribir un programa que lea un carácter correspondiente a un
# dígito hexadecimal (0..9, A..F) y lo convierta en el valor decimal
# correspondiente (0..15).
#
# COMENTARIO DE TEXTO:
# Ejercicio de TRATAMIENTO DE CARACTERES. Hay dos enfoques: (1) el manual,
# que distingue si el carácter es un dígito ('0'-'9', usando ord() y el
# código ASCII: valor = ord(c) - ord('0')) o una letra ('A'-'F', valor =
# ord(c) - ord('A') + 10); y (2) el de biblioteca: int(c, 16). Conviene
# practicar el primero y mencionar el segundo. Evalúa ord(), comparaciones
# de cadenas y validación de la entrada.
#
# Plan: validar que el carácter sea un dígito hex; convertir con ord() y
# comentar la alternativa int(c, 16).
# -----------------------------------------------------------------------------


def ejercicio_17() -> None:
    c: str = input('Dígito hexadecimal: ').upper()
    if '0' <= c <= '9':
        valor: int = ord(c) - ord('0')
    elif 'A' <= c <= 'F':
        valor = ord(c) - ord('A') + 10
    else:
        print('Error: no es un dígito hexadecimal.')
        return
    print(f'Valor decimal: {valor}')
    # Alternativa con la biblioteca estándar: valor = int(c, 16)


# -----------------------------------------------------------------------------
# EJERCICIO 18
# Enunciado: Para hallar en qué fecha cae el Domingo de Pascua de un año
# cualquiera, se calculan:
#     a = (19 * (anyo % 19) + 24) % 30
#     b = (2 * (anyo % 4) + 4 * (anyo % 7) + 6 * a + 5) % 7
# y ese domingo es el 22 de marzo + a + b días (podría caer en abril).
# Escribir un programa que realice estos cálculos, con entrada y salida
# claras.
#
# COMENTARIO DE TEXTO:
# Ejercicio de TRADUCCIÓN DE UN ALGORITMO dado (cálculo de Pascua, "algoritmo
# de Gauss/Butcher" simplificado). No hay que inventar nada: basta traducir
# las fórmulas fielmente y resolver la parte interesante, que es la gestión
# de la FECHA resultante: sumar a + b días al 22 de marzo puede desbordar el
# mes (marzo tiene 31 días), cayendo en abril. Se puede resolver con
# aritmética de fechas (datetime.date + timedelta) o manualmente: dia =
# 22 + a + b; si dia > 31, es mes = abril y dia -= 31. Evalúa operadores
# % y //, condicionales y, opcionalmente, el módulo datetime.
#
# Plan: leer el año, calcular a y b, sumar los días al 22 de marzo con
# datetime (o manualmente) y mostrar la fecha.
# -----------------------------------------------------------------------------


from datetime import date, timedelta


def ejercicio_18() -> None:
    anyo: int = int(input('Año: '))
    a: int = (19 * (anyo % 19) + 24) % 30
    b: int = (2 * (anyo % 4) + 4 * (anyo % 7) + 6 * a + 5) % 7
    pascua: date = date(anyo, 3, 22) + timedelta(days=a + b)
    print(f'El Domingo de Pascua de {anyo} cae el {pascua.day} de '
          f'{pascua.strftime("%B")} de {anyo}.')


# -----------------------------------------------------------------------------
# PROGRAMA PRINCIPAL: descomentar la llamada al ejercicio que se quiera
# probar.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # ejercicio_1()
    # ejercicio_2()
    # ejercicio_3()
    # ejercicio_4()
    # ejercicio_5()
    # ejercicio_6()
    # ejercicio_7()
    # ejercicio_8()
    # ejercicio_9()
    # ejercicio_10()
    # ejercicio_11()
    # ejercicio_12()
    # ejercicio_13()
    # ejercicio_14()
    # ejercicio_15()
    # ejercicio_16a()
    # ejercicio_16b()
    # ejercicio_16c()
    # ejercicio_16d()
    # ejercicio_17()
    ejercicio_18()
    pass