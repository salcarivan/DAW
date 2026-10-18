**Desarrollo de Aplicaciones Web IES Doñana Página 1 de 17**

**Miguel Ángel García Blanes** **IES Doñana**

# Sistemas de almacenamiento de la información

# Contenido de la unidad

### 1 Introducción ___________________________________________________________________ 3

### 2 Ficheros _______________________________________________________________________ 3

**2.1 Tipos de fichero según su estructura de almacenamiento __________________________ 4**

**2.2 Tipos de soporte de almacenamiento _____________________________________________ 5**

### 3 Bases de datos ________________________________________________________________ 5

**3.1 Definición _______________________________________________________________________ 6**

**3.2 Tipos de bases de datos __________________________________________________________ 6**

### 4 Sistemas Gestores de Bases de Datos (SGBD / DBMS) ____________________________ 8

### 5 Componentes de un SGBD _____________________________________________________ 8

| 5.1 | Lenguajes _______________________________________________________________________ 8 |
| --- | --- |
| 5.2 | Utilidades________________________________________________________________________ 9 |
| 5.3 | Diccionario de Datos _____________________________________________________________ 9 |
| 5.4 | El Gestor de la Base de Datos (o Monitor)__________________________________________ 9 |
| 5.5 | El Administrador de la Base de Datos (DBA)_______________________________________ 10 |
| 5.6 | Los Usuarios de la Base de Datos _________________________________________________ 10 |

### 6 Funciones de los SGBD ________________________________________________________ 11

| 6.1 | Función de Definición o Descripción (DDL): _______________________________________ 11 |
| --- | --- |
| 6.2 | Función de Manipulación (DML) _________________________________________________ 11 |
| 6.3 | Función de Control ______________________________________________________________ 11 |

### 7 Big Data y la inteligencia de negocios _________________________________________ 12

### 8 Legislación Vigente sobre Protección de Datos _________________________________ 13

| 8.1 | Reglamento General de Protección de Datos (RGPD - UE 2016/679)________________ 13 |
| --- | --- |
| 8.2 | Ley Orgánica 3/2018 (LOPDGDD - España) _______________________________________ 13 |
| 8.3 | Aplicación en el Ámbito de las Bases de Datos ___________________________________ 13 |
| 8.4 | Derechos de los Ciudadanos ____________________________________________________ 14 |
| 8.5 | Consecuencias del Incumplimiento ______________________________________________ 14 |

### 9 Anexo________________________________________________________________________ 15

**9.1 Tipos de gestión de un Sistemas de Información __________________________________ 15** 9.1.1 Sistemas de Información Orientados al Proceso _________________________________________ 15

9.1.2 Sistemas de Información Orientados a los Datos ________________________________________ 16

**Desarrollo de Aplicaciones Web IES Doñana Página 3 de 17**

## 1 Introducción

Según el Diccionario de la Real Academia Española (DRAE), la **informática** es el “Conjunto de conocimientos científicos y técnicas que hacen posible el tratamiento automático de la información por medio de ordenadores”.

Definimos **sistema de información** como el conjunto de elementos que trabajan juntos para **recoger,** **procesar, almacenar y distribuir información**. Su objetivo principal es ayudar a las personas o empresas a **tomar decisiones, coordinar actividades y controlar procesos**.

Antes de que existieran las bases de datos, la información se manejaba con archivos/ficheros creados especialmente para cada programa. Cada aplicación se enfocaba en cómo procesar los datos, no en cómo organizarlos. Como no había un formato estándar, cada sistema usaba sus propios archivos personalizados. Se decía entonces que las **aplicaciones** estaban **orientadas al proceso.**

Era frecuente que una organización dispusiera de varias aplicaciones que, en algunos casos, trataban la misma información. Por ejemplo, el software utilizado por el departamento de recursos humanos debía gestionar un fichero con datos de empleados, mientras la aplicación de contabilidad mantenía otro fichero distinto con los mismos datos organizados de otra forma. Esta situación acarreaba una serie de problemas tales como:

**Redundancia de datos**, es decir, duplicidad innecesaria de información. Mal aprovechamiento del **espacio de almacenamiento**. **Aumento en el tiempo de proceso**. **Inconsistencia de información** debida a la redundancia, si un dato cambiaba en el fichero de una aplicación, no cambiaba en los demás. **Aislamiento de la información.** Es complejo compartir datos entre aplicaciones. (habría que desarrollar un software de migración específico).

En resumen, todo esto hacía que el sistema fuera poco flexible y dependiera demasiado de cómo estaban guardados físicamente los datos.

## 2 Ficheros

En los años 70, las empresas se enfocaban principalmente en tareas como la contabilidad y la facturación. Para guardar y organizar la información, usaban pocos archivos en papel, ordenados en archivadores.

Cuando empezó la informatización, los datos pasaron del papel al ordenador, lo que permitió acceder a ellos mucho más rápido. Para facilitar esta transición, los programas informáticos imitaron los elementos que se usaban manualmente, como ficheros, formularios y carpetas, …

La información tenía que digitalizarse y guardarse para luego poder consultarla o procesarla después. Para hacerlo bien, era necesario usar métodos adecuados de almacenamiento. El elemento clave para guardar datos de forma permanente en dispositivos como discos duros o pendrives fue el **fichero o** **archivo**.

**Fichero** o **archivo**: conjunto de datos relacionados, organizados de forma estructurada, que se guarda como una unidad. En realidad es una secuencia de bytes (dígitos binarios), que se almacena en una memoria secundaria (disco duro, pendrive, cinta magnética, DVD,…) y a la que se hace referencia mediante un nombre.

**Nota:** Hemos de resaltar que los datos de un fichero están almacenados de tal forma que se puedan añadir, suprimir, actualizar o consultar individualmente en cualquier momento.

### 2.1 Tipos de fichero según su estructura de almacenamiento

En relación con su contenido, encontramos los siguientes tipos básicos de ficheros:

- **Fichero plano**. Almacenan secuencias de caracteres correspondientes a una codificación de terminada (ASCII, Unicode, EBCDIC, etc.). Son legibles mediante un software de edición de texto como el Bloc de Notas de Windows o el vi o nano de Linux. Almacenan datos en forma de texto simple sin ningún formato especial Ejemplos: los ficheros de texto con extensión .txt, los .csv de valores separados por comas, los .htm/ .html correspondientes a páginas web, los de lenguajes de marcas .xml …
- **Binarios**. Contienen información codificada en binario para su procesamiento por parte de aplicaciones. Su contenido resulta ilegible en un editor de texto. Ejemplos: archivos ejecutables .exe, documentos de aplicaciones .pdf, .docx, .xlsx, .pptx, ficheros de imagen, audio o video .jpg, .gif, .mp3, .avi, .mkv, archivos de sistema .dll, …

Cuando se utilizan ficheros de texto plano para almacenar información se pueden clasificar de acuerdo con su organización interna:

- **Secuenciales.** La información se escribe en posiciones físicamente contiguas. Para acceder a un dato hay que recorrer todos los anteriores.

**Fichero secuencial con información sobre clientes**

0078952lT#Paula#Sanz#González#619554687$50687452Y#José Luis#Garcia#Viñals#66785921$38546998X#Javier#Peinado#Martín#66932541$09653801B#Ruth #Lázaro#Cardenal#689330247%

Por cada contacto se ha decidió estructurar la información en cinco datos independientes: NIF, nombre, primer apellido, segundo apellido y número de teléfono. Fíjate que en este caso el programador ha decidido utilizar la almohadilla (#) como separador de datos, el dólar ($) como separador de contactos y el tanto por ciento (%) como marca de fin de fichero.

- **De acceso directo o aleatorio**. Cada registro se organiza con unos tamaños fijos de datos. Se puede acceder directamente al principio de cada registro.

**Fichero de acceso directo con información sobre clientes**

| 0078952lT | Paula | Sanz | González | 619554687 |
| --- | --- | --- | --- | --- |
| 50687452Y | José Luis | García | Viñals | 667859215 |
| 38546998X | Javier | Peinado | Martín | 669325412 |
| 09653801B | Ruth | Lázaro | Cardenal | 689330247 |

En esta ocasión, cada contacto ocupa una línea del fichero (al final de cada una, el sistema operativo incluirá uno o dos caracteres de salto de línea invisibles para el usuario), y cada dato utiliza un número de caracteres fijo, aunque no lo ocupe totalmente (en el ejemplo se reservan 15 caracteres para el nombre, aunque en el caso de Ruth solo se utilicen 4). Como todos los clientes ocupan el mismo espacio en el fichero, podemos acceder fácilmente a cualquiera de ellos multiplicando la posición en la que se encuentra menos una, por el número de caracteres que mide cada línea. Por ejemplo, si el fichero se ha creado en un sistema Windows y queremos acceder al tercer cliente, tendremos que restar uno a su posición (3 - 1=2) y multiplicar el valor resultante por la longitud de la línea (63 caracteres más los dos caracteres de salto de línea que incluye el sistema operativo, es decir. 65), Como 2 x 65 = 130, la información del tercer cliente se encontrará en la posición 131. La contrapartida a esta facilidad de posicionamiento es que el tamaño del fichero crece considerablemente respecto a su versión secuencial.

- **Indexados**. Generalmente en un fichero de acceso aleatorio la información se almacena en el orden en que se da de alta. Incluso aunque se consiguiera introducir dicha información de acuerdo con algún criterio de ordenación concreto, en algunas ocasiones es útil poder ordenarla por varios criterios distintos. En el ejemplo anterior es posible que necesitemos un listado de clientes ordenado por NIF y otro por apellido. Para dar solución a este problema se creó la **organización indexada**, que consiste en la existencia de uno o varios archivos adjuntos que ordenan el dato (**llamado clave**) por el que se desea ordenar el fichero y lo relacionan con la localización de la línea correspondiente.

En la imagen anterior los NIF aparecen ordenados. Tras cada uno de ellos se ha añadido el número de línea del fichero principal donde se encuentra la información asociada. Si una aplicación software quisiera listar los clientes ordenados por NIF, recorrería secuencialmente el fichero de índice, y al final de cada línea encontraría la línea del fichero principal que debe leer para encontrar a cada cliente. El siguiente fichero indexaría los clientes ordenados por su primer apellido:

### 2.2 Tipos de soporte de almacenamiento

De acuerdo con la organización física de los datos, diferenciamos entre dos tipos de soportes:

- **Secuenciales**. Para acceder a un dato hay que recorrer todo el contenido del soporte previo a dicho dato (ejemplo: cintas magnéticas).
- **Direccionables**. Se puede acceder directamente a un dato sin tener que recorrer todos los anteriores (ejemplo: disco duro).

**Nota:** En un soporte direccionable se puede implementar un acceso secuencial, directo o indexado, mientras que en un soporte secuencial sólo se podrá implementar un acceso secuencial.

## 3 Bases de datos

La evolución lógica de los problemas derivados del uso de ficheros fue estandarizar el acceso a la información, de modo que un diseño físico concreto sirviera para todas las aplicaciones de una organización. **Este nuevo enfoque se centraba en los datos y no en el proceso**, es decir, se estructuraba el almacenamiento de dichos datos con independencia de las aplicaciones que los fueran a utilizar. De esta forma se eliminaba la redundancia y se favorecía la transferencia de información entre aplicaciones. Esta evolución es la que da origen al concepto de **base de datos**.

| 0078952lT | 1 |
| --- | --- |
| 09653801B | 4 |
| 38546998X | 3 |
| 50687452Y | 2 |

| 0078952lT | Paula | Sanz … |
| --- | --- | --- |
| 50687452Y | José Luis | García … |
| 38546998X | Javier | Peinado … |
| 09653801B | Ruth | Lázaro … |

| García | 2 |
| --- | --- |
| Lázaro | 4 |
| Peinado | 3 |
| Sanz | 1 |

| 0078952lT | Paula | Sanz … |
| --- | --- | --- |
| 50687452Y | José Luis | García … |
| 38546998X | Javier | Peinado … |
| 09653801B | Ruth | Lázaro … |

### 3.1 Definición

De acuerdo con el DRAE, una **base de datos** se define como “Conjunto de datos organizado de tal modo que permita obtener con rapidez diversos tipos de información”.

Sin embargo, en el ámbito académico y técnico se entiende de manera más amplia. Una base de datos es un conjunto de datos relacionados entre sí, organizados de forma estructurada y almacenados en un soporte que no se pierde al apagar el ordenador (soporte no volátil). Estos datos se gestionan de manera que puedan ser utilizados por diferentes usuarios y aplicaciones al mismo tiempo, sin depender directamente de ellos.

La forma en que los datos se organizan sigue un **modelo de datos**, que permite representar no solo los datos, sino también las relaciones y reglas que existen en el mundo real. Además, la base de datos cuenta con procedimientos definidos para actualizar y recuperar la información de manera eficiente y segura, garantizando así la integridad y la coherencia de toda la información almacenada.

### 3.2 Tipos de bases de datos

Podemos elegir distintos criterios para clasificar las bases de datos, entre los más comunes destacamos:

- Atendiendo a la **variabilidad de la información almacenada**: o **Base de datos estáticas**: Son bases de datos que **no cambian con el tiempo**. Se usan para guardar información histórica, como estadísticas o registros pasados. Esta información sirve para **analizar tendencias**, hacer **proyecciones**, tomar **decisiones** **estratégicas** y apoyar la **inteligencia empresarial**. Ejemplo: una base de datos con los resultados de ventas de los últimos 10 años o **Bases de datos dinámicas**: Son bases de datos donde la información almacenada se actualiza constantemente, permitiendo operaciones como actualización, borrado y edición de datos, además de las operaciones fundamentales de consulta. Ejemplo: una base de datos que registra los pedidos de clientes en tiempo real
- Atendiendo al modelo de datos en el que está basado y que veremos más adelante. o **Bases de datos jerárquicas:** Son las más antiguas y almacenan la información en una estructura jerárquica que podemos imaginar con una forma de árbol invertido, donde cada nodo padre puede tener diferentes hijos. El nodo superior, que no tiene padre, se conoce como raíz. Y los nodos que no tienen hijos se llaman hojas. Este tipo de base de datos es muy fácil de implementar, pero dependiendo del tipo de consultas que se vaya a realizar, puede ser poco eficiente, ya que para acceder a un determinado registro es necesario acceder previamente por el nodo padre. Por otro lado, y más grave, es que sólo nos permite representar relaciones de tipo uno a varios (1:N), cosa que no siempre ocurre en la vida real; y para poder evitar esto tendríamos que añadir redundancia de datos con su posible pérdida de la integridad. Actualmente XML se basa en este tipo de estructura arborescente. o **Bases de datos de red:** Este tipo de base de datos, utiliza una estructura muy similar a la anterior para almacenar la información. Al igual que en la estructura jerárquica, cada nodo puede tener varios hijos, pero, a diferencia de ésta, también puede tener varios padres. Aunque este tipo de bases de datos supusieron una mejora respecto al modelo jerárquico, porque permitía controlar de manera más eficiente el problema de la redundancia de datos, llevaba asociada una mayor complejidad en la administración de las bases de datos.

o **Bases de datos relacionales:** Representa la información en forma de entidades y relaciones entre ellas, evitando rutas preconcebidas para localizar los datos y huyendo de la rigidez de los modelos previos. Cada entidad y cada relación aparece en forma de tablas bidimensionales (con filas y columnas). Es el modelo más extendido desde hace décadas. Ejemplos de base de datos basados en este modelo: MySQL. o **Bases de datos orientadas a objetos:** En este tipo de bases de datos, la información se representa mediante objetos como los presentes en la programación orientada a objetos. Las bases de datos orientadas a objetos se diseñan para trabajar bien en conjunción con lenguajes de programación orientados a objetos como Java, C#, Visual Basic, .NET y C++. o **Bases de datos objeto-relacional:** En los últimos años los fabricantes de bases de datos relaciónales han incorporado a su software diversas capacidades de las bases de datos orientadas a objetos, creando modelos híbridos con base relacional. Este nuevo tipo de bases de datos admite la posibilidad de que los tipos de datos sean, además de los tradicionales, tipos abstractos de datos (TAD – datos + operaciones asociadas). Con esta particularidad, se acercan los sistemas de BD relaciónales al paradigma de la programación orientada a objetos. Ejemplos: Oracle, Microsoft SQL Server, IBM Informix, PostgreSQL. o **Bases de Datos NoSQL (No solo SQL):** Son una alternativa a las bases de datos tradicionales (relacionales). Se crearon para manejar **grandes volúmenes de datos**, **información variada** (no estructurara) y **cambios rápidos**, como los que se generan en redes sociales, apps móviles o sistemas en tiempo real Los tipos comunes de bases de datos NoSQL incluyen bases de datos de documentos (como MongoDB), bases de datos de clave-valor (como Redis), bases de datos de grafos (como Neo4j) y bases de datos de columnas amplias (como Cassandra).

- Atendiendo a la ubicación física de la información: o **Centralizadas.** La base de datos reside en una sola máquina, típicamente el servidor de base de datos. o **Distribuidas.** La información se reparte por distintos servidores, generalmente alejados físicamente. Un ejemplo sería la base de datos de una compañía de seguros, concebida a partir de los datos de la oficina central y de las de todas sus sucursales. Su implantación exige hacer un fuerte hincapié en aspectos de networking y seguridad. Los Sistemas de Base de Datos distribuidos, deben encargarse de convertir las consultas globales del usuario en consultas definidas sobre **fragmentos de la base de datos**. Del mismo modo, el sistema también se encarga de mezclar las consultas fragmentadas para obtener la repuesta a una consulta global. La **fragmentación** en una base de datos distribuida consiste en la partición de una tabla de la base de datos en diferentes fragmentos. Se pueden distinguir las siguientes variantes:

| ▪ | Fragmentación vertical: la tabla se descompone en columnas (campos) |
| --- | --- |
| ▪ | Fragmentación horizontal: la tabla se descompone en filas (registros) |
| ▪ | Fragmentación mixta: Es una mezcla de las dos anteriores |

**CURIOIDAD:**

En gráficos, esquemas y literatura informática las bases de datos se representan mediante un cilindro apoyado en su base. Es una referencia a las antiguas memorias de tambor magnético, de similar aspecto físico.

## 4 Sistemas Gestores de Bases de Datos (SGBD / DBMS)

Un **sistema gestor de bases de datos (SGBD),** es una colección de programas, lenguajes, y otras herramientas que proporcionan al usuario de la base de datos los medios necesarios para realizar las siguientes tareas:

**Definición de los datos:** descripción de la base de datos. **Manipulación de los datos** almacenados en la base de datos, es decir, la inserción, modificación, borrado y acceso o consulta a los mismos. **Mantenimiento de la integridad de la BD**. Integridad en cuanto a los datos en sí, sus valores y las relaciones entre ellos. **Control de la privacidad y seguridad** de los datos en la BD. Y, en definitiva, los medios necesarios para el establecimiento de todas aquellas características exigibles a una BD. **Nota:** En el mercado hay una amplia tipología de SGBD que corresponde con el modelo de base de datos correspondiente.

## 5 Componentes de un SGBD

El **Sistema de Gestión de Bases de Datos** (**SGBD** o **DBMS**) está dividido en módulos que llevan a cabo sus funciones asociadas.

Se componen del **núcleo**, **lenguajes** que permiten la definición de la estructura de la base de datos y la manipulación de datos, **utilidades** encargadas de mejorar la presentación de la información y del **diccionario de datos**, cuyo papel es fundamental en los SGBD.

### 5.1 Lenguajes

El SGBD proporciona lenguajes que permiten la definición y manejo de los datos. Cada SGBD tiene una estructura y organización particular, pero todos tienen la característica común de ofrecer al administrador y a los usuarios dos lenguajes:

**Lenguaje de Descripción de los Datos (DDL):** Lenguaje que permite la representación lógica de los datos. La representación de los datos obtenida en este proceso de compilación es almacenada en otro componente del SGBD denominado **Diccionario de Datos**. Además, el DDL cuenta con un sublenguaje encargado del control y seguridad de los datos, el cual se denomina **Lenguaje de Control de Datos** (DCL) y permite el control del acceso de a la información almacenada en el diccionario de datos (definición de privilegios y tipos de acceso). **Nota:** Los DDL son **autocontenidos** y no necesitan apoyarse en ningún lenguaje de programación. **Lenguaje de Manipulación de Datos (DML):** Lenguaje mediante el que se realiza: la manipulación de los datos (insertar, eliminar y modificar registros) y la recuperación de la información. Se trata de un lenguaje basado en una gramática completa, sencilla y, generalmente, fácil de entender por usuarios no expertos. **Nota:** Los SGBD también son capaces de procesar peticiones de DML que se han formulado desde programas escritos en otros lenguajes de programación como Cobol, C, Pascal, Java, PHP, etc.

### 5.2 Utilidades

Son aplicaciones que facilitan el trabajo a los usuarios y programadores. Tienen la característica común de tener un interfaz fácil de entender. Se basan en menús que guían al usuario para conseguir el objetivo final.

La mayoría de los SGBD incluyen:

**Generador de menús**: Diseña la interfaz de usuario de una aplicación. **Generador de Informes**: Presenta datos en pantalla o impresora con un formato predefinido o fácil de definir sin conocer lenguajes de BD o programación. **Generador de Formularios**: Genera pantalla de diálogos que permiten la introducción sencilla de información. **Herramientas para la exportación e importación** de datos a o desde otros sistemas. **Herramientas para la creación y restablecimiento de copias de seguridad**. Es una de las tareas fundamentales, ya que permite recuperar la información en caso de pérdida de datos. **Herramientas de recuperación** en caso de desastre. Si ocurre un mal funcionamiento del sistema, un fallo en la alimentación del sistema, errores de red, etc. En ese caso los buenos SGBD poseen y proporcionan mecanismos para que se recupere la máxima información posible y se asegure su integridad.

### 5.3 Diccionario de Datos

Es un almacén integrado (conjunto de ficheros), en el que se almacena toda la información referente a la descripción, gestión e implantación de la BD. También se conoce como **catálogo del sistema**.

Se trata de una **metabase de datos**; es decir, una base de datos que contiene información sobre otra base de datos.

En el diccionario de datos se almacenan todas las definiciones realizadas por el DDL sobre el problema que va a ser tratado por el SGBD y, algunas (las que se deseen) de las realizadas por el DML.

Así, el diccionario contiene, entre otras cosas:

Descripción del esquema de la base de datos. Las restricciones de privacidad y acceso a los datos almacenados en la BD. Estas restricciones han sido definidas haciendo uso del DDL y/o su sublenguaje, el DCL. Las operaciones que realizan los usuarios en el sistema, etc.

### 5.4 El Gestor de la Base de Datos (o Monitor)

También denominado **monitor**, es un componente software (núcleo) encargado de garantizar el correcto, seguro, íntegro y eficiente acceso y almacenamiento de los datos.

Es el encargado de proporcionar una interfaz entre los datos almacenados y los programas de aplicación que los manejan.

Puede verse al gestor de la BD como un intérprete entre el usuario y los datos. Toda operación que se realice contra la BD debe de ser previamente permitida por el gestor de la misma, el cual, una vez interpretada y validada, o bien realiza la operación devolviendo el resultado de la misma al programa/procedimiento que la solicitó, o bien la rechaza.

Así tendremos que el gestor se encargará de:

**Garantizar la privacidad de los datos**. Permitiendo acceder a los datos, sólo a los usuarios autorizados. **Garantizar la seguridad de los datos**, realizando los procedimientos necesarios para que los datos puedan ser recuperados tras un fallo. **Garantizar la integridad de los datos**, de forma que los datos almacenados en la BD satisfagan las restricciones definidas en el esquema de esta. **Garantizar el acceso concurrente a la BD**, de forma que varios usuarios puedan acceder al mismo o distinto dato sin que ello ocasione una pérdida de integridad de la BD. **Interaccionar con el sistema operativo** y, en particular con el gestor de archivos de este, de forma que los procedimientos DML puedan ser entendidos por el sistema operativo para el correcto almacenamiento y recuperación de la información. Es uno de los componentes más complejos del SGBD, aunque su complejidad dependerá del propio SGBD y de las características del sistema operativo y hardware en el cual se implante.

### 5.5 El Administrador de la Base de Datos (DBA)

Se trata de un componente humano de suma importancia en el funcionamiento eficiente y fiable de la BD. El DBA va a tener una serie de responsabilidades en cuanto a la definición, administración, seguridad, privacidad e integridad de la información que es tratada.

### 5.6 Los Usuarios de la Base de Datos

Dependiendo del modo de interactuar con la base de datos podemos distinguir tres tipos de usuarios:

**Usuarios Técnicos / Expertos** o **programadores de** **aplicaciones**: son los encargados de escribir aplicaciones que hacen uso de la base de datos mediante el uso de llamadas al SGBD incrustadas en el código de un lenguaje de alto nivel (p.e. Pascal, C, PHP, Java, …). Estas aplicaciones serán usadas por los usuarios “ingenuos” o habituales.

**Usuarios normales o habituales:** son usuarios sin conocimiento en BD que utilizan las aplicaciones previamente escritas para interactuar con la base de datos (p.e. cajeros automáticos, formulario de consulta en una página web, …)

**Usuarios ocasionales:** usuarios con ciertos conocimientos que realizan consultas en la BD de forma directa mediante el uso de un lenguaje de consulta (DML)

## 6 Funciones de los SGBD

Las funciones esenciales en un SGBD son la **definición**, **manipulación** y **control**. A continuación, vamos a ver más en detalle estas tres funciones.

### 6.1 Función de Definición o Descripción (DDL):

La función de definición o descripción debe permitir al diseñador de la BD especificar los elementos de datos que la integran, su estructura y las relaciones que existen entre ellos, las reglas de integridad semántica, los controles de acceso, las características de tipo físico, etc.

Para realizar esta función se emplea el **Lenguaje de Definición de Datos (DDL)** propio de cada SGBD. La ejecución de instrucciones DDL, suelen llevar asociado cambios en el **diccionario de datos**.

**Nota:** La función de definición sirve para crear, eliminar o modificar metadatos.

### 6.2 Función de Manipulación (DML)

La función de manipulación permite a los usuarios de la base de datos recuperar o actualizar los datos, siempre de acuerdo con las especificaciones y normas de seguridad dictadas por el administrador, controlando también la concurrencia. Esta función se llevará a cabo por medio del **“Lenguaje de** **Manipulación de datos”** (DML).

### 6.3 Función de Control

Mediante esta función los administradores poseen mecanismos para proteger los datos (acceso, copia de seguridad, …). De manera que se permite a cada usuario ver ciertos datos y otros no, o bien usar ciertos recursos concretos de la base de datos y prohibir otros. Es decir, es la función encargada de establecer los permisos de acceso a los elementos que forman parte de la base de datos.

El lenguaje que implementa esta función es el “**lenguaje de control de datos” (DCL)**

## 7 Big Data y la inteligencia de negocios

El concepto de **Big Data** se refiere a la **gestión y análisis de conjuntos de datos extremadamente** **voluminosos, complejos y variables** que superan la capacidad de las herramientas de procesamiento de datos tradicionales. Estos conjuntos de datos grandes pueden incluir una variedad de tipos de información, como datos estructurados, semiestructurados y no estructurados, y **se caracterizan por** lo que se conoce comúnmente como **las "tres V"**: volumen, velocidad y variedad:

- **Volumen:** Los datos generados y almacenados en la actualidad son enormes en cantidad. Esto incluye datos de redes sociales, registros de transacciones, datos de sensores, registros de servidores, datos de aplicaciones, … El volumen de datos excede lo que las herramientas de procesamiento tradicionales pueden manejar fácilmente.
- **Velocidad:** Los datos se generan y se actualizan a una velocidad asombrosa. Esto es especialmente cierto para aplicaciones en tiempo real, como las redes sociales y los sensores IoT (Internet de las cosas). El análisis de datos a esta velocidad es un desafío significativo.
- **Variedad**: Los datos provienen de una amplia variedad de fuentes y pueden ser de diferentes tipos, como texto, imágenes, audio, video, datos geoespaciales y más. Estos datos pueden estar estructurados (como datos en una base de datos relacional), semiestructurados (como documentos XML o JSON) o no estructurados (como publicaciones en redes sociales o correos electrónicos).

El análisis de Big Data se realiza generalmente utilizando tecnologías y herramientas avanzadas, como sistemas de almacenamiento distribuido, bases de datos NoSQL, frameworks de procesamiento en clúster (por ejemplo, Hadoop y Apache Spark), técnicas de aprendizaje automático y visualización de datos. El objetivo principal del análisis de Big Data es descubrir patrones, tendencias y conocimientos valiosos que pueden ayudar a las organizaciones a tomar decisiones informadas y estratégicas.

Relacionado con el Big Data tenemos la **Inteligencia de Negocios** (Business Intelligence, BI). Este concepto se refiere a un conjunto de procesos, tecnologías y herramientas que permiten a las organizaciones **recopilar**, **analizar**, **interpretar** y **presentar datos** empresariales con el objetivo de tomar decisiones informadas y estratégicas. El propósito principal de la inteligencia de negocios es convertir los datos brutos en información significativa y útil que pueda respaldar la toma de decisiones efectivas en una organización.

Las principales características y componentes de la inteligencia de negocios incluyen:

- **Recopilación de Datos**: La BI implica la recopilación de datos de diversas fuentes, tanto internas como externas a la organización. Estos datos pueden incluir información de sistemas transaccionales, bases de datos, aplicaciones empresariales, fuentes en línea y más.
- **Almacenamiento y Organización de Datos**: Los datos se almacenan en bases de datos específicamente diseñadas para la BI. Estos almacenes suelen estar optimizados para el análisis y pueden incluir datos estructurados, semiestructurados y no estructurados.
- **Procesamiento y Transformación de Datos**: Los datos se procesan y transforman para que sean coherentes y útiles para el análisis. Esto puede incluir la limpieza de datos, la integración de datos de diferentes fuentes y la transformación de datos en formatos adecuados.
- **Análisis de Datos:** El análisis de datos es una parte central de la BI. Involucra el uso de herramientas y técnicas para explorar, visualizar y analizar datos con el objetivo de identificar patrones, tendencias, relaciones y oportunidades de mejora.
- **Generación de Informes y Paneles**: La BI permite la creación de informes y paneles de control que resumen la información clave de manera clara y comprensible. Estos informes pueden presentarse en tablas, gráficos, ...
- **Toma de Decisiones:** La información derivada del análisis de datos se utiliza para respaldar la toma de decisiones estratégicas en una organización. Esto puede incluir decisiones relacionadas con ventas, marketing, operaciones, finanzas y gestión de recursos humanos, entre otros.

- **Predicción y Modelado**: La BI avanzada puede incluir técnicas de modelado predictivo que permiten a las organizaciones anticipar tendencias futuras y tomar decisiones proactivas.
- **Acceso Seguro a los Datos**: La seguridad y el acceso controlado a los datos son fundamentales en la BI para proteger la información sensible y cumplir con regulaciones y políticas de privacidad.

## 8 Legislación Vigente sobre Protección de Datos

En el contexto del tratamiento de datos personales a través de bases de datos, es imprescindible conocer y aplicar la legislación vigente en materia de protección de datos. Este documento tiene como objetivo identificar y explicar las principales normativas legales que regulan el uso, almacenamiento, acceso y protección de los datos personales, con especial atención a su implicación en el diseño y gestión de bases de datos.

### 8.1 Reglamento General de Protección de Datos (RGPD - UE 2016/679)

El **Reglamento General de Protección de Datos (RGPD)**, en vigor desde el 25 de mayo de 2018, es la principal normativa a nivel europeo que regula la protección de los datos personales de los ciudadanos de la Unión Europea. Tiene aplicación directa en todos los estados miembros, incluido España.

**Aspectos clave del RGPD:**

- **Licitud del tratamiento:** Los datos personales deben ser tratados de forma lícita, leal y transparente.

| • | Finalidad: Los datos deben ser recogidos con fines determinados, explícitos y legítimos. |
| --- | --- |
| • | Minimización de datos: Solo se deben recoger los datos estrictamente necesarios. |
| • | Exactitud: Los datos deben mantenerse actualizados. |
| • | Limitación del plazo de conservación: Los datos no deben conservarse más tiempo del |

necesario.

- **Integridad y confidencialidad:** Se debe garantizar la seguridad adecuada mediante medidas técnicas y organizativas.

### 8.2 Ley Orgánica 3/2018 (LOPDGDD - España)

En España, el RGPD se complementa con la **Ley Orgánica 3/2018, de Protección de Datos Personales y** **garantía de los derechos digitales (LOPDGDD)**. Esta ley adapta el contenido del RGPD al ordenamiento jurídico español e introduce medidas específicas, como:

| • | Regulación del derecho a la desconexión digital en el ámbito laboral. |
| --- | --- |
| • | Mayor desarrollo del derecho al olvido. |
| • | Normas sobre el tratamiento de datos por parte de entidades públicas y empresas. |
| • | Especificación de los deberes del Delegado de Protección de Datos (DPO). |

### 8.3 Aplicación en el Ámbito de las Bases de Datos

El cumplimiento de la legislación de protección de datos en bases de datos implica diversas acciones:

- **Diseño de bases de datos seguras**: con controles de acceso, cifrado de datos sensibles, y separación de datos según niveles de confidencialidad.
- **Principio de privacidad desde el diseño**: la protección de datos debe integrarse desde la planificación de cualquier sistema que recoja o procese datos personales.
- **Consentimiento informado**: la recogida de datos debe basarse en el consentimiento explícito del usuario o en otra base legal válida.
- **Auditorías y registros de tratamiento**: las organizaciones deben llevar un control documental sobre qué datos tratan, cómo lo hacen, y con qué finalidad.

### 8.4 Derechos de los Ciudadanos

Tanto el RGPD como la LOPDGDD reconocen una serie de **derechos a los titulares de los datos** **personales**, que deben poder ejercerse fácilmente:

| • | Derecho de acceso |
| --- | --- |
| • | Derecho de rectificación |
| • | Derecho de supresión ("derecho al olvido") |
| • | Derecho a la limitación del tratamiento |
| • | Derecho a la portabilidad de los datos |
| • | Derecho de oposición |
| • | Derecho a no ser objeto de decisiones automatizadas |

### 8.5 Consecuencias del Incumplimiento

El incumplimiento de estas normativas puede suponer **sanciones económicas muy elevadas**, además de daños a la reputación de la organización. Las multas bajo el RGPD pueden alcanzar hasta **20** **millones de euros o el 4% de la facturación anual global**, lo que ocurra primero.

## 9 Anexo

### 9.1 Tipos de gestión de un Sistemas de Información

En la evolución de los sistemas de información, ha habido dos puntos determinantes, que han formado los dos tipos fundamentales de sistemas de información.

**9.1.1 Sistemas de Información Orientados al Proceso** Antes de aparecer los **Sistemas Gestores de Bases de Datos** **(SGBD),** en la década de los setenta, la información se trataba y se gestionaba utilizando los típicos sistemas de gestión de archivos que iban soportados sobre un sistema operativo. Estos consistían en un conjunto de programas que definían y trabajaban sus propios datos. Los datos se almacenan en archivos y los programas manejan esos archivos para obtener la información. Si la estructura de los datos de los archivos cambia, todos los programas que los manejan se deben modificar; por ejemplo, un programa trabaja con un archivo de datos de alumnos, con una estructura o registro ya definido; si se incorporan elementos o campos a la estructura del archivo, los programas que utilizan ese archivo se tienen que modificar para tratar esos nuevos elementos. En estos sistemas de gestión de archivos, la definición de los datos se encuentra codificada dentro de los programas de aplicación en lugar de almacenarse de forma independiente, y además el control del acceso y la manipulación de los datos viene impuesto por los programas de aplicación.

Esto supone un gran inconveniente a la hora de tratar grandes volúmenes de información. Surge así la idea de separar los datos contenidos en los archivos de los programas que los manipulan, es decir, que se pueda modificar la estructura de los datos de los archivos sin que por ello se tengan que modificar los programas con los que trabajan. Se trata de estructurar y organizar los datos de forma que se pueda acceder a ellos con independencia de los programas que los gestionan.

En resumen, cada aplicación almacena y utiliza sus propios datos de forma un tanto caótica. La ventaja de este sistema (la única ventaja), es que los procesos son independientes por lo que la modificación de uno no afecta al resto. Pero tiene grandes inconvenientes:

**Programación de aplicaciones compleja**. Ya que los programadores se deben de encargar de lo que tiene que hacer la aplicación y además de estructurar los datos en disco. **Datos redundantes.** Se produce porque los archivos son creados por distintos programas y van cambiando a lo largo del tiempo, es decir, pueden tener distintos formatos y los datos pueden estar duplicados en varios sitios. Por ejemplo, el teléfono de un alumno puede aparecer en más de un archivo. La redundancia aumenta los costes de almacenamiento y acceso, y trae consigo la **inconsistencia de los datos**. **Datos inconsistentes**. En relación con el problema anterior, ya que un proceso cambia sus datos y no los del resto. Por lo que la misma información puede tener distintos valores según qué aplicación acceda a él. **Dificultad para tener acceso a los datos.** Cada vez que se requiera una consulta no prevista inicialmente, hay que modificar el código de las aplicaciones, o incluso crear una nueva aplicación. Esto hace imposible pensar en nuevas consultas e instantáneamente obtener sus resultados. Es inviable para aplicaciones que requieren grandes capacidades de consultas y análisis de datos.

**Coste de almacenamiento elevado.** Al almacenarse varias veces el mismo dato, se requiere más espacio en los discos. Además, las aplicaciones también ocupan mucho al tener que pensar en todas las posibles consultas sobre los datos que la organización precisa. **Dependencia de los datos física-lógica**, o lo que es lo mismo, la estructura física de los datos (definición de archivos y registros) se encuentra codificada en los programas de aplicación. Para poder saber cómo se almacenan los datos, es decir qué estructura se utiliza de los mismos, necesitamos ver el código de la aplicación; es decir el código y los datos no son independientes. **Dificultad para el acceso concurrente**. El acceso simultáneo requiere que varios usuarios puedan acceder a la misma información. Con este tipo de sistemas es extremadamente difícil conseguir esta capacidad. Las actualizaciones concurrentes pueden dar por resultado datos inconsistentes, ya que se puede acceder a los datos por medio de diversos programas de aplicación. **Problemas en la seguridad de los datos.** Resulta difícil implantar restricciones de seguridad pues las aplicaciones se van añadiendo al sistema según se van necesitando.

Todos estos inconvenientes hacen posible el fomento y desarrollo de **SGBD**. El objetivo primordial de un gestor es proporcionar eficiencia y seguridad a la hora de extraer o almacenar información en las BD. Los SGBD están diseñados para gestionar grandes bloques de información, que implica tanto la definición de estructuras para el almacenamiento como de mecanismos para la gestión de la información.

Se consideran también sistemas de gestión de ficheros, a los sistemas que utilizan programas ofimáticos (como Word o Excel por ejemplo) para gestionar sus datos. Esta última idea, la utilizan muchas pequeñas empresas para gestionar los datos, debido al presupuesto limitado del que disponen. Gestionar la información de esta forma produce los mismos (si no más) problemas.

**9.1.2 Sistemas de Información Orientados a los Datos** En este tipo de sistemas los datos se centralizan en una **base de datos** común a todas las aplicaciones. Estos serán los sistemas que estudiaremos en este curso.

En esos sistemas los datos se almacenan en una única estructura lógica que es utilizable por las aplicaciones. A través de esa estructura se accede a los datos que son comunes a todas las aplicaciones.

**Ventajas de los sistemas orientados a los datos**

**Independencia de los datos y los programas**. Esto permite modificar los datos sin modificar el código de las aplicaciones. **Menor redundancia.** No hace falta tanta repetición de datos. Sólo se indica la forma en la que se relacionan los datos. **Integridad de los datos**. Mayor dificultad de perder los datos o de realizar incoherencias con ellos. **Mayor seguridad en los datos**. El SGBD es el encargado de la seguridad y se puede centrar en ella de forma independiente a las aplicaciones. Como las aplicaciones deben atravesar la capa del SGBD para llegar a los datos, no se podrán saltar la seguridad. **Visiones distintas según el usuario**. Nuevamente, centralizar los datos facilita crear políticas que permitan que los usuarios vean la información de la base de datos de forma distinta. **Datos más documentados**. Gracias a los **metadatos** que permiten describir la información de la base de datos. **Acceso a los datos más eficiente**. La organización de los datos produce un resultado más óptimo en rendimiento. **Menor espacio de almacenamiento**. Gracias a una mejor estructuración de los datos.

**Acceso simultáneo a los datos**. Es más fácil controlar el acceso de usuarios de forma concurrente.

**Inconvenientes de los sistemas orientados a los datos**

**Instalación costosa.** El control y administración de bases de datos requiere de un software y hardware poderoso **Requiere personal cualificado.** Debido a la dificultad de manejo de este tipo de sistemas. **Implantación larga y difícil.** Debido a los puntos anteriores. La adaptación del personal es mucho más complicada y lleva bastante tiempo. **Ausencia de estándares reales.** Lo cual significa una excesiva dependencia hacia los sistemas comerciales del mercado. Aunque, hoy en día, una buena parte de esta tecnología está aceptada como estándar de hecho.