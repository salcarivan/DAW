**Miguel Ángel García Blanes** **IES Doñana**

# Diseño de BD Relacionales. Modelo E-R

# Contenido de la unidad

1 Introducción ...........................................................................................................................................3 2 Diseño conceptual: El Modelo Entidad-Relación (E/R) ......................................................................3

2.1 Componentes del modelo ..............................................................................................................................4 2.1.1 Entidad ...................................................................................................................................................................4

2.1.2 Relación..................................................................................................................................................................5

2.1.3 Atributos.................................................................................................................................................................8

2.1.4 Dependencia en existencia y en identificación .....................................................................................................10

3 Modelo E/R Extendido.........................................................................................................................11

3.1 Relaciones IS A o relaciones de jerarquía. ................................................................................................11 3.1.1 Características ......................................................................................................................................................11

3.1.2 Tipos de Generalización .......................................................................................................................................11 3.2 Restricción de Exclusividad y Exclusión ...................................................................................................12 3.3 Restricciones de Inclusividad e Inclusión ..................................................................................................13

4 Control de redundancia .......................................................................................................................13

4.1 Atributos derivados .....................................................................................................................................13 4.2 Interrelaciones redundantes .......................................................................................................................13

## 1 Introducción

Crear una BD es un proceso complejo que parte de la necesidad de almacenar información del mundo real. A continuación, estableceremos los conceptos y técnicas necesarias para diseñar bases de datos eficientes.

Está claro que necesitaremos de una metodología lo suficientemente potente, para llegar a conseguir unos resultados óptimos. Esta metodología la podríamos dividir en las siguientes fases:

- Diseño Conceptual Es el primer paso en el diseño de bases de datos. Este diseño es independiente del sistema gestor de la base de datos usado y del ordenador. Simplemente estudiamos el problema, y seleccionamos qué elementos del mundo real vamos a modelar, es decir, es una representación abstracta y simplificada del conjunto de datos de una organización, enfocada en cómo se estructuran y relacionan dichos datos sin entrar en detalles técnicos de implementación. Este diseño, corresponde en el caso de las bases de datos relaciónales, al modelo Entidad-Relación (también conocido como E/R, modelo E-R, ...)
- Diseño Lógico Es un puente entre el diseño conceptual y el diseño físico. Consiste en una transformación del modelo obtenido en el diseño conceptual. Esta transformación daría como resultado un modelo que se podría implementar en SGBD específico, pero aún de forma independiente de los detalles técnicos del hardware o del software de base de datos. En nuestro caso este modelo será el modelo relacional. Adicionalmente, será necesario comprobar que el modelo lógico resultante garantiza las propiedades de eliminación de redundancias, fácil accesibilidad a los datos, etc. Para ello, en el caso de bases de datos relaciónales, recurriremos a la teoría de la normalización, que nos permitirá obtener las mejores relaciones posibles para un esquema lógico.
- Diseño Físico Este diseño sí depende del ordenador, sistema gestor de base de datos usado, etc. En este caso, empleando el gestor de la base de datos implementamos nuestra base de datos en función de lo que nos marca el diseño lógico.

## 2 Diseño conceptual: El Modelo Entidad-Relación (E/R)

En este apartado estudiaremos el modelo E/R, uno de los modelos de datos conceptuales más extendidos en las metodologías de diseño de bases de datos y en las herramientas CASE.

El modelo E/R fue propuesto por Peter P. Chen en 1976 para la representación conceptual de los problemas del mundo real. Según Chen, el modelo E/R puede ser usado como una base para una vista unificada de los datos, adoptando el enfoque más natural del mundo real que consiste en entidades y relaciones.

Posteriormente, otros autores han investigado y escrito sobre el modelo, proponiendo importantes aportaciones, por lo que realmente no se puede considerar que exista un único modelo E/R, sino más bien lo que podríamos llamar una familia de modelos. La más aceptada actualmente es el modelo entidad/relación extendido (ERE) que complementa algunas carencias del modelo original.

Hay que insistir en que este modelo no tiene nada que ver con las bases de datos relacionales, los esquemas entidad/relación se pueden utilizar con cualquier SGBD ya que son conceptuales. Confunde el uso de la palabra relación, pero el concepto de relación en este esquema no tiene nada que ver con la idea de relación expuesta por Codd en su modelo relacional.

**2.1 Componentes del modelo**

**2.1.1 Entidad** Una entidad es cualquier objeto real o abstracto que tiene existencia por sí mismo y se puede identificar de una forma clara y precisa, y del cual se desea registrar información en el sistema. Es el elemento fundamental que hay que caracterizar. Se representa con sustantivos en singular que encierran un concepto, y es labor del analista identificar dichos sustantivos. Ejemplos de entidad: “Empleado". “Cliente", “Factura",...

La entidad es un concepto abstracto y cada elemento concreto de una entidad es una ocurrencia. En el ejemplo de la entidad “Empleado", cada uno de los empleados es una ocurrencia de dicha entidad.

A su vez, cada ocurrencia presenta una serie de datos asociados. Un empleado tendrá nombre, apellidos. NIF, dirección postal, número de teléfono, etc. Cada uno de esos datos es un atributo, y cada ocurrencia tiene distintos valores para cada atributo (en la entidad “Empleado”, un empleado concreto tendrá “Juan Antonio" como valor de su atributo “Nombre”, “García Corredor” como valor de su atributo “Apellidos”, y 52871660Y como valor de su atributo “NIF”

Toda entidad debe cumplir dos características:

- Presencia del mismo conjunto de atributos para todas las ocurrencias, independiente mente de que alguna ocurrencia carezca de valor para algún atributo.
- Diferenciación univoca de ocurrencias. No puede haber dos ocurrencias con los mismos valores para todos sus atributos.

2.1.1.1 Representación gráfica de las entidades En el modelo entidad relación, las entidades se representan con un rectángulo dentro del cual se escribe el nombre de la entidad (generalmente en mayúsculas).

Los atributos asociados a una entidad se pueden representar de dos formas: mediante óvalos que incluyen el nombre del atributo o mediante círculos con el nombre del atributo en el exterior:

2.1.1.2 Tipos de entidades Podemos distinguir los siguientes tipos de entidades:

- Fuerte o regular. Son las entidades normales que tienen existencia por sí mismas sin depender de otras. Su representación gráfica es la indicada arriba.
- Débil. Su existencia depende de otras. Supongamos un sistema de información de una biblioteca. Si queremos llevar un control sobre las sanciones impuestas a los socios por devolución tardía de libros, crearemos una entidad “SANCIÓN". Toda sanción se impone a un socio; por tanto, no podrá haber ocurrencias en la entidad “SANCIÓN" si no existe una ocurrencia correspondiente a un socio en la entidad “SOCIO”. Las entidades débiles se representan mediante un doble rectángulo.

Para que una entidad sea débil ha de serlo respecto a todas las entidades con las que se relaciona.

PERSONA

**2.1.2 Relación** Una relación representa una asociación entre entidades. Es el elemento del modelo que permite relacionar en sí los datos de este. Por ejemplo, en el caso de que tengamos una entidad “PARSONA” y otra entidad “PROFESIÓN”. Ambas se relacionan ya que, las personas trabajan y los trabajos son realizados por personas.

En una relación, cada ejemplar asocia un elemento de una entidad con otro de la otra entidad. En una relación no pueden aparecer dos veces relacionados los mismos ejemplares. Es decir, en el ejemplo anterior, en la relación no puede aparecer dos veces el mismo trabajador asociado al mismo trabajo. 2.1.2.1 Representación gráfica La representación gráfica de una relación se realiza con un rombo al que se le unen líneas que se dirigen a las entidades. Las relaciones tienen nombre (se suele usar un verbo). En el ejemplo anterior podría usarse como nombre de relación, trabajar. 2.1.2.2 Tipos de relaciones Atendiendo al número de entidades cuyas ocurrencias se relaciones, podemos encontrar los siguientes tipos de relaciones.

- Relaciones Binarias. Son las relaciones típicas. Se trata de relaciones que asocian dos entidades.
- Relaciones Ternarias. Relacionan ocurrencias de tres entidades. A veces se pueden simplificar en relaciones binarias, pero no siempre es posible.
- Relaciones n-arias. Relacionan n entidades. Dependiendo de la complejidad de nuestro modelo de datos, podemos relacionar ocurrencias de más de tres entidades.
- Relaciones dobles. Se llaman así a dos relaciones distintas que sirven para relacionar a las mismas entidades. Son las más difíciles de manejar ya que al manipular las entidades hay que elegir muy bien la relacionan a utilizar para relacionar los datos.
- Relación reflexiva. Es una relación que sirve para relacionar ejemplares de la misma entidad (personas con personas, piezas con piezas, etc.). Para comprenderlas correctamente hay que tener en cuenta que las ocurrencias que relacionan, aun perteneciendo a la misma entidad, están jugando papeles distintos.

PERSONA PROFESIÓN

PERSONA Trabaja PROFESIÓN

2.1.2.3 Cardinalidad La cardinalidad de una relación es el número de ocurrencias de una entidad asociadas a una ocurrencia de otra entidad. Sirve para conocer el grado de participación de las entidades en una relación.

La cardinalidad indica el número máximo de ocurrencias de una entidad con las que se puede relacionar de otra entidad. Es posible que en nuestro sistema de información toda factura deba emitirse a nombre de un solo cliente, pero que cada cliente pueda emitir muchas facturas; puede que cada proveedor suministre varios artículos y que cada artículo sea suministrado por varios proveedores; y quizás cada empleado se siente en una ubicación concreta de la oficina y a cada ubicación corresponda solamente un empleado. La cardinalidad refleja esta casuística del siguiente modo:

- Uno a uno (1:1): A cada ocurrencia de la entidad A le corresponde, como máximo, una ocurrencia de la entidad B, y viceversa

- Uno a muchos (1:N): A cada ocurrencia de la entidad A le pueden corresponder varias ocurrencias de la entidad B. Pero a cada ocurrencia de la entidad B sólo le corresponde, como máximo, una ocurrencia de la entidad A.

- Muchos a muchos (M:N): A cada ocurrencia de la entidad A le pueden corresponder varias ocurrencias de la entidad B. Y a cada ocurrencia de la entidad B le pueden corresponder varias ocurrencias de la entidad A

Para obtener la cardinalidad de una relación, se debe fijar una ocurrencia en concreto de una entidad y averiguar cuántas ocurrencias de la otra entidad le corresponden. Después, realizar lo mismo en el otro sentido.

La cardinalidad delimita los límites superiores de una relación, pero no define su obligatoriedad. ¿Todo instrumento debe ser tocado por algún músico? ¿Podría haber alguna ocurrencia en la entidad “Instrumento” que no tuviera relación con otra ocurrencia en la entidad “Músico”?. Puede que, como requisito del sistema de información, la entidad “Instrumento” deba contener una lista de instrumentos independientemente de que haya algún músico que los toque (quizás una de las ocurrencias de “Instrumento" corresponda al acordeón y, en cambio, en “Músico” no haya ninguna ocurrencia correspondiente a un músico que toque el acordeón). Pero también puede que el sistema de información exija que las ocurrencias de “Instrumento” se carguen a medida que se introduzcan en “Músico" ocurrencias de músicos, de modo que todos los instrumentos tendrían su correspondencia con, al menos, un músico. Obviamente, las dos situaciones son incompatibles en un buen diseño de datos, y la cardinalidad no nos aporta la información necesaria para solventar esta disyuntiva. Hemos de abordar un nuevo concepto.

La modalidad (llamada por algunos autores cardinalidad, con la consiguiente confusión, o participación) define el número mínimo y máximo de ocurrencias de una entidad que pueden estar relacionadas con una ocurrencia de otra u otras entidades, identificando relaciones optativas (en las que no tiene por qué haber correspondencia). La modalidad / participación se indica a ambos lados de la relación, y su valor máximo coincide con el valor de la cardinalidad correspondiente al lado de la relación en el que nos encontremos. Puede ser de los siguientes tipos:

- (0,1) (cero a uno). Cada ocurrencia de la primera entidad puede relacionarse con una ocurrencia de la segunda entidad o no. No puede relacionarse con varias.
- (1,1) (uno a uno). Cada ocurrencia de la primera entidad debe relacionarse obligatoriamente con una y sólo una ocurrencia de la segunda entidad.

- (1,n) (uno a ene / uno a muchos). Cada ocurrencia de la primera entidad debe relacionarse obligatoriamente con al menos una ocurrencia de la segunda entidad. Puede relacionarse con varias.
- (0,n) (cero a ene / cero a muchos). Cada ocurrencia de la primera entidad no tiene limitada su relación con ocurrencias de la segunda entidad. Puede relacionarse con una, varias, o ninguna.

Veamos el siguiente ejemplo, correspondiente a un concesionario de automóviles:

Para cada entidad de la relación debemos leer su modalidad en el lado opuesto. En este caso, la modalidad de “Cliente” con respecto a “Automóvil” es de (0,n), y la de “Automóvil” con respecto a “Cliente” es de (0,1). Esta relación “compra” se leería del siguiente modo:

- Toda ocurrencia de “cliente” puede relacionarse con vanas ocurrencias de "Automóvil", con una, o con ninguna. En lenguaje natural: un cliente puede no comprar, comprar un automóvil o comprar varios automóviles.
- Toda ocurrencia de “Automóvil” puede relacionarse con una sola ocurrencia de “Cliente” o no (un automóvil puede ser vendido a un solo cliente, o bien no ser vendido; en cualquier caso, el mismo automóvil no puede ser vendido a varios clientes).

Este otro ejemplo refleja una situación diferente

Al igual que en el caso anterior, la cardinalidad es 1:N, pero la modalidad / participación es más restrictiva: (1,n) de “Grupo” a “Alumno” y (1,1) de “Alumno” a “Grupo”

- Toda ocurrencia de “Grupo” está obligada a relacionarse con al menos una ocurrencia de “Alumno”, pudiendo relacionarse con varias (todo grupo de alumnos debe tener alumnos).
- Toda ocurrencia de “Alumno” está obligada a relacionarse con una y solo una ocurrencia de “Grupo” (cada alumno debe pertenecer de forma obligatoria a un grupo y solamente a uno).

Analicemos ahora un caso de modalidad sobre una cardinalidad de M:N. Imaginemos un sistema de información de una biblioteca donde a los socios se les da de alta en el momento en que retiran su primer libro en préstamo (por tanto, en el sistema no puede haber socios a los que no se haya prestado un libro):

La interpretación sería:

- Toda ocurrencia de “Socio” está obligada a relacionarse con al menos una ocurrencia de “Libro”, y puede relacionarse con varias (todo socio debe haber recibido al menos un libro en préstamo).
- Toda ocurrencia de “Libro” puede relacionarse con varias ocurrencias de “Socio”, con una o con ninguna (un libro puede haber sido prestado a un socio, a varios o a ninguno).

Nótese que, una vez que se utiliza el concepto de modalidad, no es necesario indicar la cardinalidad, ya que esta se puede deducir a partir de aquella (tomando los valores máximos a cada lado de la relación).

En las relaciones ternarias y n-arias la modalidad se lee de una forma algo distinta. La indicación de modalidad correspondiente a cada entidad indica cómo se relacionan las ocurrencias de dicha entidad con una vinculación de ocurrencias del resto de las entidades participantes en la relación. Veamos el siguiente ejemplo:

- El (1,n) de “Aula” indica que la combinación profesorgrupo-asignatura puede ocurrir en una o vanas aulas (un profesor puede impartir una asignatura a un grupo en un aula o en varias, obviamente, en momentos diferentes en el tiempo.
- El (0,n) “Asignatura” nos dice que por cada ocurrencia de la relación profesor-grupo-aula puede haber una, varias o ninguna asignatura (un profesor puede impartir vanas asignaturas al mismo grupo en la misma aula, pero también puede reunirse en un aula con un grupo para llevar a cabo una tarea que no sea impartir una asignatura (por ejemplo, una reunión de tutoría).
- El (1,n) “Grupo” implica que todo profesor que imparte una asignatura en un aula la puede impartir a uno o varios grupos (es decir, puede impartir la misma asignatura a varios grupos en la misma aula)
- El (1,1) de “Profesor” quiere decir que un profesor y solamente uno puede impartir la misma asignatura al mismo grupo en la misma aula.

2.1.2.4 Roles A veces en las líneas de la relación se indican roles. Los roles representan el papel que juega una entidad en una determinada relación. Son imprescindibles cuando las relaciones son complejas, ya que ayudan a entender el sentido de la relación.

Ejemplo: Un trabajador puede ser visto como jefe o como empleado según a qué lado de la relación esté. En ese caso la lectura sería:

- Un trabajador es jefe de uno, varios o ningún empleado
- Un trabajador es empleado de ningún o un jefe.

**2.1.3 Atributos** Describen propiedades de las entidades y las relaciones. Como comentamos en un apartado anterior, se puede representar mediante óvalos que incluyen el nombre del atributo o mediante círculos con el nombre del atributo en el exterior.

2.1.3.1 Tipos de Atributos Podemos encontrarnos con distintos tipos de atributos, entre los que destacamos los siguientes

Simples y compuestos.

- Simples: Son atributos que no están formados por otros atributos.
- Compuestos: son atributos que a su vez pueden ser simples o compuestos. La forma de representarlo será:

(0,n)

TRABAJADOR Trabaja

Monovaluados y multivaluados

- Monovaluados: son atributos que representan un valor para una determinada ocurrencia de una entidad en un momento determinado. Pueden ser simples o compuestos.
- Multivaluados: son atributos que pueden representar varios valores simultáneamente para una misma ocurrencia de una entidad (pueden ser simples o compuestos). Se representan mediante un doble óvalo, o mediante la cardinalidad de la relación como se verá un poco más adelante.

Derivados (o calculados): son atributos cuyo valor se obtiene aplicando una fórmula (normalmente a partir del valor de otros atributos). Son atributos que no se almacenarán en la base de datos. Su valor se obtendrá en el momento en que sea necesario, aplicando la fórmula asociada a ellos. Se representan en un diagrama ER mediante un óvalo con línea discontinua, o con línea discontinua entre entidad/relación y atributo.

Propios: son los atributos de las relaciones. Se representan unidos al rombo de la relación

Identificadores: Se trata de uno o más campos cuyos valores son únicos en cada ejemplar de una entidad. Toda entidad debe tener al menos un atributo identificador. Los atributos identificadores pueden ser simples o compuestos.

- Identificador primario e identificadores alternativos: Una entidad puede tener más de 1 atributo identificador; en ese caso, elegimos un atributo como identificador primario (P), quedando el resto como identificadores alternativos (A).
- Los atributos identificadores simples se representan subrayando el nombre del atributo, o rellenando el círculo del atributo.

- Los identificadores alternativos se representan con la letra A sobre (o al lado de) la línea que une la entidad con el atributo

2.1.3.2 Cardinalidades de atributo Para cada atributo de una entidad se puede especificar una cardinalidad (min, max); la cual indicará cuantos valores puede almacenar el atributo para una ocurrencia determinada de la entidad.

Por defecto (si no ponemos nada), la cardinalidad de un atributo asociado a una entidad es (1,1); es decir, el atributo debe obligatoriamente tener exactamente un valor para toda ocurrencia de la entidad.

Nota: Para atributos multivaluados la cardinalidad por defecto es (1,n).

Pondremos como cardinalidad de atributo (0,1) si queremos indicar que un atributo puede contener un valor nulo.

Para atributos compuestos, si no especificamos nada, entonces es obligatorio que tengan valor todos sus atributos componentes. Si especificamos una cardinalidad para un atributo compuesto, pero no para los atributos componentes, entonces todos los atributos componentes "heredan" esa cardinalidad. Por ejemplo: si pusiéramos (0,1) como cardinalidad del atributo DIRECCIÓN, entonces todos sus componentes podrían contener un valor nulo.

Para atributos multivaluados podemos especificar un rango finito. Por ejemplo: para el atributo multivaluado compuesto TELEFONO podemos decir que su cardinalidad es (0,3), de tal manera indicamos que una persona puede tener de 0 a 3 teléfonos como máximo.

**2.1.4 Dependencia en existencia y en identificación** Este tipo de relaciones se nos presenta cuando relacionamos una entidad fuerte con una entidad débil.

Recordemos que una entidad débil es aquella que su existencia depende la existencia de otra entidad (fuerte)

Toda entidad débil tiene una dependencia en existencia de la entidad de orden superior, definiéndose entre ellas una jerarquía de dos niveles.

Normalmente, la entidad débil con restricción de existencia suele tener una clave primaria propia que permite establecer de forma independiente la asociación de la ocurrencia de la entidad débil a través de la interrelación establecida entre ambas. Convienen resaltar aquí que la interrelación mencionada tendrá carnalidad 1:N. En la siguiente figura puede apreciarse un ejemplo de este tipo de entidades.

Por el contrario, la dependencia en identificación se produce cuando una entidad no es identificable por el valor de sus atributos, pero sí por su interrelación con otra entidad; por tanto, son un caso particular de las anteriores. En este caso, la clave primaria de la entidad débil se forma por unión de la Clave primaria de la entidad fuerte con el/los atributos descriptores / discriminadores de la entidad débil. En la figura siguiente puede apreciarse un ejemplo de este tipo de entidades. En este caso, el atributo NÚMERO por sí solo no permite distinguir cada una de las ocurrencias de la entidad EJEMPLAR (porque sus valores se repiten para ejemplares de libros distintos), es decir, NÚMERO no es clave / identificador de la entidad EJEMPLAR. Será ISBN como clave de la entidad fuerte LIBRO más NÚMERO como discriminador de la entidad EJEMPLAR.

## 3 Modelo E/R Extendido

El modelo E/R con el paso del tiempo ha sufrido una serie de modificaciones tanto en su simbolismo gráfico, como en la ampliación de sus elementos.

**3.1 Relaciones IS A o relaciones de jerarquía.**

Son relaciones que indican tipos de entidades, es decir tendremos entidades que son un (is a, en inglés) tipo de entidad.

Se utilizan para unificar entidades agrupándolas en una entidad más general (generalización) o bien para dividir una entidad general en entidades más específicas (especificación). Aunque hoy en día a todas se las suele llamar generalización e incluso relaciones de herencia.

Se habla de generalización si inicialmente partimos de una serie de entidades que al estudiarlas en detalle descubrimos que todas ellas pertenecen al mismo conjunto, que será el que determine una nueva entidad. En la generalización las entidades son totalmente heterogéneas, es decir, los atributos son diferentes. La entidad general se llama superentidad, y el resto se denominan subentidades. En la superentidad se colocan los atributos comunes a todas las subentidades. Y normalmente se la coloca una clave principal distinta de las subentidades.

La especialización ocurre cuando partimos de una entidad que podemos dividir en subentidades para detallar atributos que varían en las mismas. Comparten clave con la superentidad y los atributos de la superclase se heredan en las subclases.

En la práctica se manejan casi igual ambas; la forma de representar una IS A es mediante un triángulo invertido, con la base paralela al rectángulo que representa la superentidad (o supertipo).

**3.1.1 Características**

- Toda ocurrencia de un subtipo es una ocurrencia del supertipo, las cardinalidades serán siempre (1,1) en el supertipo y (0,1) ó (1,1) en los subtipos.
- Todo atributo del supertipo pasa a ser un atributo de los subtipos.

Así, en el ejemplo, podemos establecer una asociación entre la entidad EMPLEADO y las entidades DOCENTE y NO DOCENTE en el sentido de que tanto los docentes como los no docentes son tipos de empleados, por lo que heredaran todas las características de la entidad EMPLEADO (código, nombre, dirección, sueldo, etc.).

En este tipo de abstracción, los atributos comunes a todos los subtipos se asignan al supertipo, mientras que los atributos específicos se asocian al subtipo correspondiente.

Las relaciones que afectan a todos los subtipos se asocian al supertipo, dejándose para los subtipos las relaciones específicas en las que el correspondiente subtipo participa.

**3.1.2 Tipos de Generalización** Se pueden distinguir cuatro tipos de generalización, atendiendo a si los subtipos se solapan o son disjuntos, y a si la unión de los subtipos recubre o no el supertipo.

Jerarquía Total y Disjunta (exclusiva):

- Tanto un docente como un no docente son empleados.
- Un mismo empleado no puede ser a la vez docente y no docente. (exclusiva o disjunta)
- Todo empleado tiene que ser obligatoriamente un docente o un no docente (total)

Jerarquía Parcial y Disjunta (exclusiva):

| ▪ | Tanto un artículo como un libro son documentos. |
| --- | --- |
| ▪ | Un mismo documento no puede ser a la vez un artículo y un libro (exclusividad). |
| ▪ | Puede haber documentos que no sean ni artículos ni libros (Parcialidad). |

Jerarquía Total con solapamiento:

| ▪ | Tanto un empleado como un estudiante son personas. |
| --- | --- |
| ▪ | Una misma persona puede ser estudiante a la vez que empleado |
| ▪ | Toda persona en nuestra BD tiene que ser obligatoriamente un estudiante y/o |

empleado

Jerarquía Parcial con solapamiento:

| ▪ | Tanto un docente como un investigador son empleados. |
| --- | --- |
| ▪ | Un mismo empleado puede ser, y en general lo es, docente a la vez que investigador. |
| ▪ | Puede haber empleados que no seas ni docentes ni investigadores. |

**3.2 Restricción de Exclusividad y Exclusión**

Decimos que dos (o más) tipos de interrelación tienen una restricción de exclusividad con respecto a un tipo de entidad que participa en ambas interrelaciones cuando cada ejemplar de dicho tipo de entidad sólo puede pertenecer a uno de los tipos de la interrelación, pero en el momento en que pertenezca a uno ya no podrá formar parte del otro. Por ejemplo, si suponemos que un profesor puede impartir cursos de doctorado o recibirlos, pero no ambas cosas, tendríamos una interrelación Imparte y otra Recibe, entre PROFESOR y CURSO, con una restricción de exclusividad entre sí. En la figura adjunta se muestra la representación de la exclusividad. El arco señala las interrelaciones que son exclusivas.

El significado de la figura es el siguiente: un profesor puede impartir o no cursos de doctorado (0,n), y puede o no recibirlos (0,n), pero si un profesor imparte estos cursos no puede recibirlos y viceversa. Un curso de doctorado es impartido por un solo profesor (1,1), pero a él pueden asistir varios profesores o ninguno (0,n).

No es obligatorio que las interrelaciones exclusivas lo sean respecto al mismo tipo de entidad (en este caso CURSO), sino que podrían serlo respecto a distintos tipos. Véase, el siguiente ejemplo, donde si un profesor percibe una beca no puede estar contratado en un proyecto.

La restricción de exclusividad en el ejemplo anterior indicaba que un profesor podía impartir o recibir cursos, pero no ambas cosas; si el profesor no es doctor podrá recibir cursos de doctorado y en caso contrario impartirlos. Supongamos ahora que se permite a un profesor ya doctor matricularse en cursos aunque él, a su vez, esté impartiendo otros cursos. En este caso la restricción que debemos imponer es que un profesor no esté impartiendo y recibiendo el mismo curso. Es decir, que todo ejemplar de profesor que esté unido a un ejemplar de curso mediante la interrelación imparte, no podrá estar unido al mismo ejemplar de curso mediante la interrelación recibe. En este caso decimos que existe una restricción de exclusión y se representa tal y como aparece en la figura.

**3.3 Restricciones de Inclusividad e Inclusión**

Supongamos ahora que se desea imponer la restricción de que sólo pueden impartir clases en nuestro programa de doctorado aquellos profesores que hayan realizado al menos un curso dentro de este mismo programa, aunque no tiene por qué ser el mismo que él imparte. Aplicamos entonces una restricción de inclusividad entre dos (o más) tipos de interrelación con respecto a uno de los tipos de entidad que participa en ambas interrelaciones, por la cual toda ejemplar de dicho tipo de entidad que participa en uno de los tipos de interrelación tiene necesariamente que participar en la otra. En la figura adjunta se muestra la notación gráfica propuesta para este tipo de interrelación.

En este ejemplo se representa que si un profesor participa en Imparte tiene que participar necesariamente en Recibe. La cardinalidad sobre la flecha de inclusividad, (3,n), indica el número mínimo y máximo de cursos que tiene que recibir un determinado profesor para que se le permita impartir cursos.

A veces es preciso imponer una restricción más fuerte: si un profesor imparte un curso es porque previamente ha tenido que recibir dicho curso. Aplicamos pues una restricción de inclusión, representada en la figura, por la cual todo ejemplar de profesor que esté unido a un ejemplar de curso mediante la interrelación imparte, tiene necesariamente que estar unido al mismo ejemplar de curso mediante la interrelación recibe Si se considera la dimensión temporal se pueden tener casos más complejos de modelado, como por ejemplo que todo profesor que imparta un curso tiene que haberlo recibido antes (restricción de inclusión con el histórico de recibe) pero no puede estar recibiéndolo a la vez que lo imparte (restricción de exclusión con el actual de recibe).

## 4 Control de redundancia

Es preciso, en los esquemas E/R, analizar la existencia de redundancias, por los problemas de inconsistencias a los que pueden dar lugar.

Decimos que un elemento de un esquema es redundante cuando puede ser eliminado sin pérdida de semántica.

Existen dos formas principales de redundancia, según el elemento del modelo E/R al que está asociada: redundancia en los atributos (atributos derivados) y redundancia en las interrelaciones (denominadas también por algunos autores interrelaciones derivadas).

**4.1 Atributos derivados**

Entendemos por atributos derivados (o calculados) aquellos que se obtienen a partir de otros ya existentes, por lo que, aunque son redundantes, no dan lugar a inconsistencias, siempre que en el esquema se indique su condición de derivados y la fórmula mediante la que han de ser calculados.

**4.2 Interrelaciones redundantes**

Se dice que una interrelación es redundante cuando su eliminación no implica pérdida de semántica porque existe la posibilidad de realizar la misma asociación de ejemplares por medio de otras interrelaciones.

Es condición necesaria, aunque no suficiente, para que una interrelación sea redundante que forme parte de un ciclo, por lo que hay que estudiar detenidamente los ciclos en el diagrama E/R.

En el ejemplo de la siguiente figura se da un ciclo entre PROFESOR, CURSO y DEPARTAMENTO, por lo que en principio es posible que aparezca alguna interrelación redundante. Supongamos que un profesor sólo puede impartir cursos de doctorado que estén adscritos al departamento al que él pertenece; en este caso, si se conocen los cursos de doctorado que imparte un profesor y el departamento al que está adscrito cada curso, se deduce inmediatamente a qué departamento pertenece dicho profesor; de forma análoga, dado un departamento, si sabemos qué cursos de doctorado tiene adscritos y los profesores que imparten dichos cursos, conoceremos qué profesores pertenecen a dicho departamento, por lo que la interrelación pertenece entre las entidades PROFESOR y DEPARTAMENTO es redundante, su eliminación no produce pérdida de información.

En la figura adjunta, a pesar de que también existe un ciclo, no hay ninguna interrelación redundante. En este ejemplo la semántica es distinta y un departamento puede no tener adscritos cursos de doctorado; además un mismo curso puede estar adscrito a distintos departamentos y puede haber profesores que no impartan ningún curso. La interrelación pertenece no puede deducirse en este caso de las otras dos, ya que aunque sepamos los cursos que ha impartido un profesor y los departamentos a los que están adscritos dichos cursos, no podemos saber a qué departamento en concreto pertenece dicho profesor; tampoco se tiene esta información para los profesores que no imparten ningún curso. La interrelación imparte tampoco es redundante, ya que un curso de doctorado puede ser impartido por diversos departamentos a cada uno de los cuales pertenecen varios profesores, por lo que no se puede saber qué profesor en concreto imparte un determinado curso. Por último, la interrelación “adscrito” tampoco es redundante, ya que un curso impartido por un profesor no tiene por qué estar necesariamente adscrito al departamento al que pertenece dicho profesor: hay departamentos que no tienen cursos adscritos y los profesores de estos departamentos pueden colaborar en cursos adscritos a otros departamentos distintos del suyo.

Existen otros casos en los que la interrelación, a pesar de poder ser deducida a partir de otras presentes en el esquema, no se puede eliminar porque posee atributos.

Se puede decir, como norma general, que la existencia de un ciclo no implica la existencia de interrelaciones redundantes. Deben estudiarse con mucho detenimiento las cardinalidades / participaciones mínimas de las entidades, así como la semántica que aportan las interrelaciones, para poder afirmar con seguridad que existen interrelaciones redundantes. Habrá que analizar si al eliminar una interrelación es siempre posible el paso, tanto en un sentido como en el inverso, entre las dos entidades unidas por la interrelación que se considera redundante, y habrá que comprobar también que no se pierdan atributos.

En resumen, para que una interrelación pueda ser eliminada por redundante se tiene que cumplir:

- Que exista un ciclo
- Que las interrelaciones que componen el ciclo sean equivalentes semánticamente
- Que se puedan asociar los ejemplares de las dos entidades que estaban interrelacionadas, aun habiéndose eliminado la interrelación
- Que la interrelación o bien no tenga atributos o bien éstos puedan ser transferidos a otra a fin de no perder su semántica.