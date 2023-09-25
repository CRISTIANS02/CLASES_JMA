# AVERIGUAR FUNCIONES DE PYTHON MAS USADAS CON EJEMPLOS  PRACTICOS   PARA    PASADO
 **FUNCION PRINT**

  Imprime en la consola de comandos
  ```python
   print('¡hola mundo!')
   ¡hola mundo!
  ```
  **FUNCION LEN**

  Debuelve la longuitud( el numero de elementos) de un objeto
  ```python
  len(['a','b','c','d','e'])  #   → .........................5
  len('¡hola mundo!')   #   → .........................11  
  ```
 **FUNCION MAX**

Devuelve el elemento más grande en un**iterable** (todos los elementos deben ser del mismo tipo) o el más grande de dos o más argumentos.
```PYTHON
max(2, 3)
3
max([1, 2, 3])
3
max('a', 'b', 'c')
'c'
```

**FUNCION MIN**

Devuelve el elemento más pequeño en un iterable o el más pequeño de dos o más argumentos.
```PYTHON
min(2, 3)
2
>>> min([1, 2, 3])
1
min('a', 'b', 'c')
'a'
```

**FUNCION DIVMOD(a,b)**


Devuelve el cociente y el sobrante de dividir dos números.
```python
divmod(5,2)
(2, 1)
divmod(13.5,2.5)
(5.0, 1.0)
```


**Función abs()**

Retorna el valor absoluto de un número.
```python
abs(5)
5
abs(-5)
5
```


 **Función complex(real, imag)**

Retorna el número complejo con el valor real + imag*1j. También convierte una cadena o un número a un número complejo.
```python
complex(5,1)
(5+1j)
complex('1+5j')
(1+5j)
complex(5j)
5j
complex(1+5j)
(1+5j)
complex(1)(1+0j)
```


**Función pow** 

(base, exp)
Retorna base elevado a exp.

```PYTHON
 pow(5,2)
25
pow(5,-2)
# Result = 1/25
0.04

```

## TAREA 2
**AVERIGUAR SOBRE ENTORNOS DE PYTHON**

## ENTORNOS VIRTUALES DE PYTHON

*Los entornos virtuales se pueden describir como directorios de instalación aislados. Este aislamiento te permite localizar la instalación de las dependencias de tu proyecto, sin obligarte a instalarlas en todo el sistema.*

Imagina que tienes dos aplicaciones, App1 y App2. Ambos usan el paquete Pak, pero requieren versiones diferentes. Si instala Pak versión 2.3 para App1, no podrá ejecutar App2 porque requiere la versión 3.1.

**Aquí es donde los entornos virtuales son útiles.**

**Beneficios:**

* Puedes tener varios entornos, con varios conjuntos de paquetes, sin conflictos entre ellos. De esta manera, los requisitos de diferentes proyectos se pueden satisfacer al mismo tiempo.
* Puedes lanzar fácilmente tu proyecto con sus propios módulos dependientes.
  
Aquí hay dos formas en las que puede crear entornos virtuales Python.

**VIRTUALENV**


Es una herramienta que se utiliza para crear entornos Python aislados. Crea una carpeta que contiene todos los ejecutables necesarios para usar los paquetes que necesitaría un proyecto de Python.

Puedes instalarlo con **pip**:
```PYTHON
pip install virtualenv
```


Verifica la instalación con el siguiente comando:
```PYTHON
virtualenv --version
```
**CREAR UN ENTORNO**

Para crear un entorno virtual utiliza:
```PYTHON
virtualenv --no-site-packages my-env
```

Esto crea una carpeta en el directorio actual con el nombre del entorno *(my-env/)*. Esta carpeta contiene los directorios para instalar módulos y ejecutables de Python.

También puedes especificar la versión de Python con la que quieres trabajar. Simplemente usa el argumento *--python=/ruta/a/la/version/de/python.* Por ejemplo, python2.7:
```PYTHON
virtualenv --python=/usr/bin/python2.7 my-env
```
**LISTA DE ENTORNOS**

Puedes enumerar los entornos disponibles con:
```PYTHON
lsvirtualenv
```

**Activar un entorno**

Antes de utilizar el entorno, debes activarlo:

```PYTHON
source my-env/bin/activate
```

Esto asegura que solo se usen los paquetes bajo *my-env/.*

Notarás que el nombre del entorno se muestra a la izquierda de la línea de comandos. De esta forma puedes ver cuál es el entorno activo.

**Instalar paquetes**

Puede instalar paquetes uno por uno o configurando un archivo *requirements.txt* para tu proyecto.

```PYTHON
pip install algun-paquete
pip install -r requirements.txt
```

Si quieres crear un archivo *requirements.txt*  a partir de los paquetes ya instalados, ejecuta el siguiente comando:
```PYTHON
pip freeze > requirements.txt
```

El archivo contendrá la lista de todos los paquetes instalados en el entorno actual y sus respectivas versiones. Esto te ayudará a lanzar tu proyecto con sus propios módulos dependientes.

**Desactivar un entorno**

Si has terminado de trabajar con el entorno virtual, puedes desactivarlo con:

```PYTHON
deactivate
```

Esto te devuelve al intérprete de Python predeterminado del sistema con todas sus bibliotecas instaladas.

**Eliminar un entorno**

Simplemente elimina la carpeta del entorno.

**Conda**

*Conda* es una gestión de paquetes, dependencias y entornos para muchos lenguajes, incluido Python.

Para instalar Conda, sigue estas instrucciones.

**Crear un entorno**
Para crear un entorno virtual, use:
```PYTHON
conda create --name my-env
```


Conda creará la carpeta correspondiente dentro del directorio de instalación de Conda.

También puedes especificar con qué versión de Python quieres trabajar:
```PYTHON
conda create --name my-env python=3.6
```

**Lista de entornos**.

Puedes enumerar los entornos disponibles con:

```PYTHON
conda info --envs
```

**Activar un entorno**

Antes de utilizar el entorno, debes activarlo:
```PYTHON
source activate my-env
```


**Instalar paquetes**

Igual que con *virtualenv.*

**Desactivar un entorno**

Si has terminado de trabajar con el entorno virtual, puedes desactivarlo con:

```PYTHON
source deactivate
```

**Eliminar un entorno**

Si quieres eliminar un entorno de Conda, utiliza:

```PYTHON
conda remove --name my-env
```
