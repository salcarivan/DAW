# Fundamentos

### Ricardo Pérez López

### IES Doñana, curso 2025/2026

Generado el 2026/05/28 a las 19:51:00

## Índice

1. **Fórmulas 2** 1.1. Fórmulas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.1.1. Igualdad . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.1.2. Proposiciones lógicas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2. **Colecciones 3** 2.1. Colecciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.2. Conjuntos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.2.1. Pertenencia a un conjunto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.2.2. Igualdad de conjuntos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.2.3. Representación de conjuntos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.2.4. Conjuntos notables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.2.5. Cardinal de un conjunto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.2.6. Subconjuntos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.3. Secuencias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.3.1. Parejas, tríos, …, tuplas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 2.3.2. Elementos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3. **Producto cartesiano 6** 3.1. Producto cartesiano . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4. **Relaciones 6** 4.1. Relaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 4.1.1. Grado de una relación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 4.1.2. Relaciones reflexivas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
5. **Funciones 7** 5.1. Funciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 5.1.1. Dominio, rango, conjunto origen y conjunto imagen . . . . . . . . . . . . . . . . 8 5.1.2. Tipos de funciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 5.1.3. Representación de funciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 5.2. Funciones de varias variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

1

Fundamentos 1. Fórmulas

## 1. Fórmulas

### 1.1. Fórmulas

Una **variable** es un símbolo que representa un valor que puede cambiar. Por ejemplo: X, x, a, total. Una **constante** es un símbolo que representa un valor que nunca cambia. Por ejemplo: 1, =, π. Muchas veces, el que un símbolo sea constante o variable depende del contexto y del acuerdo al que se haya llegado. Por ejemplo, el símbolo + puede representar varias cosas según el momento. Una **fórmula** es una secuencia de símbolos (números, letras y caracteres especiales) que tiene que cumplir unas reglas de formación determinadas por un **lenguaje formal**. En Matemáticas, las fórmulas también se denominan **expresiones matemáticas** y sirven para representar formalmente un concepto o una idea.

**1.1.1. Igualdad**

En Matemáticas, la expresión a = b representa que a y b son la misma cosa. En tal caso, decimos que a y b son **iguales**. Si no son la misma cosa, decimos que son **distintos** y se representa con la expresión a 6= b.

**1.1.2. Proposiciones lógicas**

Una **proposición**, **aserción** o **aserto** es la expresión de que ocurre un suceso. Si el suceso ocurre realmente, decimos que la proposición es **verdadera** y, en caso contrario, decimos que es **falsa**. Si siempre que una proposición J es verdadera, también lo es otra proposición K, decimos que J **implica** K, y se escribe: J =⇒ K (implicación lógica)

Cuando no sólo J implica K, sino que además K implica J, se dice que las proposiciones J y K son **lógicamente equivalentes**. En ese caso, decimos que el suceso de J ocurre si y sólo si ocurre el de K. Se escribe: J ⇐⇒ K (equivalencia lógica)

Por ejemplo, las proposiciones J = hoy es martes y K = mañana es miércoles son equivalentes.

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 2

Fundamentos 2. Colecciones

## 2. Colecciones

### 2.1. Colecciones

Una **colección** es un grupo de objetos llamados **elementos** o **componentes**. Las colecciones no tienen ninguna restricción especial. Por tanto, los elementos de una colección:

- Pueden aparecer varias veces en una colección (estar repetidos), o pueden no hacerlo.
- Pueden estar situados en un orden concreto dentro de una colección (estar ordenados), o pueden no estarlo.

Los dos grandes tipos de colecciones son los **conjuntos** y las **secuencias**.

### 2.2. Conjuntos

Un **conjunto** es una colección de elementos que cumple lo siguiente:

- Sus elementos **no están ordenados** según un orden concreto. Por tanto, no se puede hablar del «primer elemento», «segundo elemento», etcétera. Debido a eso, decimos que los elementos de un conjunto están desordenados.
- Sus elementos **no pueden estar repetidos**. Por tanto, si un elemento está en un conjunto, sólo puede estarlo una vez. Debido a eso, decimos que los elementos de un conjunto son **únicos**.

En definitiva, de un elemento de un conjunto sólo tiene sentido preguntarse si pertenece o no pertenece al conjunto, no cuantas veces está ni en qué posición.

**2.2.1. Pertenencia a un conjunto**

Si un elemento a pertenece a un conjunto C, se escribe a ∈ C. De lo contrario, se escribe a ∈ / C.

**2.2.2. Igualdad de conjuntos**

Dos conjuntos son **iguales** si tienen exactamente los mismos elementos.

**2.2.3. Representación de conjuntos**

Los conjuntos se pueden representar de varias formas:

- **Gráficamente:** mediante un **diagrama de Venn**.
- **Con una expresión:** en general, una expresión encerrada entre **llaves** {} representa un conjunto. Normalmente, las variables que representan conjuntos se escriben con mayúsculas (A, B, C, …) mientras que las letras minúsculas suelen representar elementos.

Cuando un conjunto se representa mediante una expresión, se puede representar:

- Por **extensión**.
- Por **comprensión**.

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 3

Fundamentos 2.2 Conjuntos

- Por **definición inductiva**.

**2.2.3.1. Por extensión**

Indicando sus elementos encerrados entre llaves y separados por comas:

C = {λ, 4, ⋆, 23.7}

C se compone exactamente de esos cuatro elementos.

C = {λ, 4, ⋆, 23.7, . . .}

C se compone de esos cuatro elementos y de algunos más. Normalmente, los puntos suspensivos se utilizan cuando resulta evidente cuáles son los elementos que no aparecen indicados expresamente. Por ejemplo:

C = {1, 2, 3, . . .}

es el conjunto de todos los números naturales desde el 1 en adelante. También se pueden utilizar los puntos suspensivos para expresar un rango de valores. Por ejemplo:

C = {1, 2, 3, . . . , 10}

es el conjunto de los números naturales comprendidos entre 1 y 10.

**2.2.3.2. Por comprensión**

Según alguna propiedad que cumplen los elementos. Por ejemplo: C = {a | a es un número primo menor que 10} es el conjunto {2, 3, 5, 7} El símbolo | se lee «tal que».

**2.2.3.3. Por definición inductiva**

Indicando un método que permite obtener los elementos de un conjunto de forma progresiva («hacia delante» o «de abajo arriba») a partir de los anteriores. Por ejemplo, para representar el conjunto de los números naturales podemos seguir las siguientes reglas:

1. 0 es un número natural.
2. Si n es un número natural, también lo es n + 1.
3. Sólo son números naturales los obtenidos siguiendo las reglas 1 y 2.

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 4

Fundamentos 2.3 Secuencias

**2.2.4. Conjuntos notables**

Existen varios conjuntos muy importantes en Matemáticas, tanto que tienen su propio símbolo especial para poder referirnos a ellos. Por ejemplo:

- N = {0, 1, 2, . . .}: el conjunto de los números naturales.
- N+ = {1, 2, . . .}: el conjunto N menos el cero.
- Z = {. . . , −2, −1, 0, 1, 2, . . .}: el conjunto de los números enteros.
- Q: el conjunto de los números racionales.
- R: el conjunto de los números reales.
- ∅: el **conjunto vacío**, es decir, el que no contiene ningún elemento.

**2.2.5. Cardinal de un conjunto**

El **cardinal** de un conjunto es el número de elementos que tiene. El cardinal de un conjunto C se representa |C|. Un conjunto puede ser **finito** o **infinito**. Por ejemplo, si C = {2, 3, 5, 7}, entonces |C| = 4 y, por tanto, es un conjunto finito. En cambio, |N| = ∞ y, por tanto, es un conjunto infinito. El cardinal del conjunto vacío es cero: |∅| = 0.

**2.2.6. Subconjuntos**

Un conjunto A se dice que es un **subconjunto** de un conjunto B si cada elemento de A lo es también de B. En tal caso, se escribe: A ⊆ B

Claramente, siempre se cumple que A ⊆ A. Cuando A ⊆ B y B posee algún elemento que no es de A (o, lo que es lo mismo, que A 6= B), se dice que A es un **subconjunto propio** de B y se escribe:

A ⊂ B

Está claro que A ⊆ B, B ⊆ A ⇐⇒ A = B. El conjunto vacío ∅ es subconjunto de cualquier conjunto.

### 2.3. Secuencias

Una **secuencia** es una colección de elementos que cumple lo siguiente:

- Sus elementos **están ordenados** según un determinado orden. Por tanto (dependiendo de la cantidad de elementos que contenga), hay un elemento situado en primer lugar, otro situado en segundo lugar, y así sucesivamente.
- Sus elementos **pueden estar repetidos**. Por tanto, el mismo elemento puede aparecer varias veces en la misma secuencia, en distintas posiciones.

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 5

Fundamentos 3. Producto cartesiano

**2.3.1. Parejas, tríos, …, tuplas**

Llamaremos **par** o **pareja** de dos elementos a y b (y lo escribiremos como 〈a, b〉 o como (a, b)) a una **sucesión** de dos objetos a y b, donde a está señalado como primero y b como segundo. Por tanto, en general se cumple que 〈a, b〉 6 = 〈b, a〉. Igualmente, llamamos **terna** de tres elementos a, b y c (y lo escribimos como 〈a, b, c〉) a una sucesión de tres objetos, donde a está considerado como primero, b como segundo y c como tercero. Siguiendo así, podemos definir **cuaterna**, **quíntupla**, **séxtupla**, … y, en general, **enetupla**, n**‐tupla** o, simplemente, **tupla**. Una 1‐tupla 〈a〉 se puede escribir simplemente a.

**2.3.2. Elementos**

En general, a los objetos que forman una tupla se las llama **elementos** o **componentes**. En Matemáticas, las **secuencias** se pueden escribir mediante **tuplas**.

## 3. Producto cartesiano

### 3.1. Producto cartesiano

El **producto cartesiano** de A por B es el conjunto de todos los pares 〈a, b〉 que se pueden formar tales que a ∈ A y b ∈ B. Se escribe: A × B

Por tanto, se puede definir como:

A × B = {〈a, b〉 | a ∈ A, b ∈ B}

Igualmente, se define el producto cartesiano de E1 × E2 × · · · × En como el conjunto formado por las n‐tuplas 〈e1, e2, . . . , en〉 tales que:

e1 ∈ E1, e2 ∈ E2, . . . , en ∈ En

El producto cartesiano de A por sí mismo, A × A, se puede escribir como A2. Igualmente, el producto cartesiano de n conjuntos iguales a E se suele escribir En si no hay lugar a confusión. Está claro que E1 = E.

## 4. Relaciones

### 4.1. Relaciones

Una **relación** R definida sobre los conjuntos E1, E2, . . . , En es un subconjunto del producto cartesiano E1 × E2 × · · · × En: R ⊆ E1 × E2 × · · · × En

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 6

Fundamentos 5. Funciones

Por tanto, una relación es un conjunto de tuplas formadas con los elementos de los conjuntos sobre los que se define la relación. Las relaciones, en definitiva, lo que hacen es asociar entre sí elementos de varios conjuntos.

**4.1.1. Grado de una relación**

El valor de n (es decir, el número de conjuntos sobre el que se define la relación) representa el **grado** de una relación. Si n = 1, tenemos una relación 1‐aria, que se puede considerar como un subconjunto de E1. El caso más importante es el de n = 2, es decir, el de las relaciones binarias. Por supuesto, no es necesario que todos los conjuntos sobre los que se define una relación sean distintos. De hecho, muchas de las relaciones más interesantes que existen son las que relacionan a un conjunto consigo mismo. Por ejemplo, la relación binaria R definida así:

R = {〈a, b〉 | a ∈ N, b ∈ N, a < b}

**4.1.2. Relaciones reflexivas**

Una relación binaria R definida sobre un conjunto E (es decir, que relaciona a E consigo mismo) se dice que es **reflexiva**, o que tiene la propiedad reflexiva, si para todo elemento a de E se cumple que 〈a, a〉 ∈ E.

## 5. Funciones

### 5.1. Funciones

Dados dos conjuntos A y B, una **función** o **aplicación** de A en B es un conjunto f de pares 〈a, b〉 de A × B que cumple que cada elemento de A sólo puede aparecer, como mucho, una única vez como primer componente en un par de f. Dicho de otra forma: una función es una relación binaria en la que no puede haber dos pares distintos con el mismo primer componente (el primer componente no se puede repetir en ningún par). Para indicar que f es una función de A en B, se escribe:

f : A −→ B

Se puede decir que f asocia elementos de A con elementos de B, de forma que:

- Un elemento de A puede no estar asociado con ningún elemento de B.
- Si un elemento a de A está asociado con algún elemento b de B, entonces:
- Se dice que a es el **origen** de b en f.
- Se dice que b es la **imagen** de a por f.
- b se puede expresar como f(a).

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 7

Fundamentos 5.1 Funciones

- Se puede escribir: f : a 7→ b

y se lee: «la imagen de a en f es b». Por lo dicho anteriormente, la imagen de a es única, es decir, cada elemento de A sólo puede tener una imagen como mucho (puede que ninguna).

**5.1.1. Dominio, rango, conjunto origen y conjunto imagen**

Se llama **conjunto origen** (o simplemente **origen**) de f, y se representa como orig(f), al conjunto A.

Se llama **conjunto imagen** (o simplemente **imagen**) de f, y se representa como imag(f), al conjunto B. Se llama **dominio** de f, y se representa como dom(f), al conjunto de todos los orígenes de f. Se llama **rango** o **codominio** de f, y se representa como rang(f), , al conjunto de todas las imágenes de f. Es evidente que dom(f) ⊆ A y que rang(f) ⊆ B.

**5.1.2. Tipos de funciones**

Si se cumple que dom(f) 6= A, decimos que f es una **función parcial**. En caso contrario (cuando dom(f) = A), decimos que es una **función total**. Se dice que f es **suprayectiva** (o **sobreyectiva**) si rang(f) = B, es decir, si cada elemento de B es imagen de algún elemento de A. Se dice que f es **inyectiva** si para todo a, b ∈ A, f(a) = f(b) =⇒ a = b. O, lo que es lo mismo, a 6= b =⇒ f(a) 6= f(b). Se dice que f es **biyectiva** si es inyectiva y suprayectiva al mismo tiempo.

**5.1.3. Representación de funciones**

Las funciones se pueden representar:

- **Por extensión:** enumerando sus tuplas (las funciones son conjuntos de tuplas).
- **Con ecuaciones:** expresando algebraicamente la correspondencia entre los elementos del conjunto origen y del conjunto imagen. Por ejemplo:

f : N −→ R f(x) = 1 x

donde x es la **variable independiente**. Recordemos que una función es un caso particular de relación, la cual a su vez es un conjunto de tuplas. En este caso, f(2) = 1 2 . Por tanto, la función f (como conjunto) contendrá a la tupla 〈2, 2 1 〉.

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 8

Fundamentos 5.2 Funciones de varias variables

### 5.2. Funciones de varias variables

Cuando el conjunto origen de una función es el producto cartesiano de varios conjuntos, tenemos una **función de varias variables**. Las funciones de varias variables se llaman así porque tienen varias variables independientes. En realidad, lo que hace es asociar tuplas con imágenes (que también podrían ser otras tuplas, pero ese ya es otro tema). Por ejemplo, la función que asocia cada pareja de números enteros con su suma, se podría representar así:

f : N × N −→ N f(x, y) = x + y

donde x e y son las variables independientes. En este caso, f(2, 3) = 5, así que la función f asocia a la pareja 〈2, 5〉 con el valor entero 5. Por tanto, la función f (como conjunto) contendrá a la tupla 〈〈2, 3〉, 5〉.

© Ricardo Pérez López (IES Doñana, curso 2025/2026) 9