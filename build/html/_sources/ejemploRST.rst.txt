Cabecera
========
Para escribir párrafos solo tenemos que escribir sin marcador especial.

Si queremos remarcar con *cursiva*.

Si queremos remarcar con **negrita**.

Para ejemplos de código hay que usar doble apóstrofe: ``import sys``.

**Especificaciones:**

* No puedo estar anidado.
* El contenido no puede comenzar con un espacio en blanco: * texto* no funciona.
* Tiene que estar separado por caracteres separadores. Se puede usar la barra de escape para permitir unir palabras: Esto\ **es**\ una\ **palabra**.

---------------------------------------------


Secciones
=========

Subsecciones
------------

Subsecciones
^^^^^^^^^^^^

---------------------------------------------

Los distintos niveles de sección se escriben de la siguiente forma:

* = Para secciones

* `-` Para subsecciones (sin comillas).

* ^ Para subsecciones

* " Para párrafos

---------------------------------------------

.. _listas:

LISTAS
^^^^^^

Listas desordenadas
^^^^^^^^^^^^^^^^^^^
**Un ejemplo:**

- Elemento 1
- Elemento 2
- Elemento 3

**Otro ejemplo:**

* Lista simple
* Otro elemento de la lista

 * Con subniveles
    * Otro subniveles
    * Muy facilmente

Listas ordenadas
^^^^^^^^^^^^^^^^
#. Primer elemento
#. Elemento.

 #. Con subnivel
 #. Otro subnivel

ó

- Primer elemento

  - Subelemento 1
  - Subelemento 2
- Segundo elemento

ó

#. Otro tipo de lista
#. Ordenada

-----------------------------------------------

Lista de definiciones
^^^^^^^^^^^^^^^^^^^^^
Término (primera linea de texto)
    Definición del término, que tiene que estar tabulada.

    Puede tener varias líneas o varios párrafos.

   Siguiente término.
    Con su definición.

Bloques literales
^^^^^^^^^^^^^^^^^
Después de un texto normal, podemos dejar un párrafo con un ejemplo de código poniendo doble doble punto(::)::

    def funcion (self):
        print (variable)
        return None

    def otraFuncion:
        print (otraVariable)

El texto continúa normal después del bloque.

-----------------------------------------------

Bloques de Doctest
^^^^^^^^^^^^^^^^^^^
Para los bloques de Doctest no requiere ninguna marca especial, excepto que el bloque tiene que estar precedido por un párrafo en blanco.

    >>> print ("Hola mundo")
    Hola mundo

-----------------------------------------------

Hipervínculos
^^^^^^^^^^^^^
Podemos consultar la documentación de `RestructureText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

El párrafo tiene un enlace a la página del centro `Daniel Castelao`_.

.. _Daniel Castelao: https://www.danielcastelao.org/

Enlaces Internos
^^^^^^^^^^^^^^^^
Para enlazar a un título de sección, se usa el nombre del título en minúsculas, con guiones en lugar de espacios, y precedido por dos puntos.

Por ejemplo, para enlazar a la sección "Listas", se usa `listas`_.

Tablas
^^^^^^
Las tablas se escriben con barras verticales y guiones.

+-----------------+-----------------+
| Cabecera 1      | Cabecera 2      |
+=================+=================+
| Celda 1         | Celda 2         |
+-----------------+-----------------+
| Celda 3         | Celda 4         |
+-----------------+-----------------+

========== ========== ========== ==========
Cabecera 1 Cabecera 2 Cabecera 3 Cabecera 4
========== ========== ========== ==========
Celda 1    Celda 2    Celda 3    Celda 4
Celda 5    Celda 6    Celda 7    Celda 8
========== ========== ========== ==========

Imagenes
^^^^^^^^
Las imágenes se pueden insertar con la siguiente sintaxis:

.. imagen:: _static/gatito.png