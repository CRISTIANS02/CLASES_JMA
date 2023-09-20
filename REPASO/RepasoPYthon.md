# REPASO PYTHON


## TIPOS DE DATOS
  **Tipos  de datos primitivos**
 ```python
 'a' # string cadena texto
 'hola' # esto tambien es un string
 'hola soy un string y te saludo' # cadena larga
 ```
**OBSERVACION :**  *Todo lo que este entre comillas  es un* **string**.

```python
'100'
'false'
"hola"
```
*Aun string puede estar entre comillas dobles ("") o comillas simples (´´)*
```python
100 # esto es un tipo de dato numerico entero intiger 
2.1  # Esto es un dato de tipo numerico de tipo flotante Float
```





## VARIABLES
*Es donde almacenamos nuestro tipo de dato,estos datos pueden **mutar cambiar o modificarse** como creamos una variable para almacenar nuestros datos.*
1. Darle un nombre **significativo** o relacionado al dato que estamos almacenando.
2. Indicar el tipo de dato esta relacionado → asignacion =.
3. Indicar el tipo de dato que se va almacenar → darle el dato a guardar.

```python
# primero el dato lo voy a pedir la edad a nadine
edad_nadine=18

#El nombre de un alumno
 nombre_alumno='Edwin'
```

## OPERADORES
1. Existen los operadores aritmetico
 * suma 
 * resta
 * multiplicacion
 * divicion
  
 **SUMA**
```PYTHON
Suma = 45+12
```
**RESTA**
```PYTHON
Resta = 45-12
```
**MULTIPLICACION**
```PYTHON
Multiplicacion =45*12
```
**DIVICION**
```PYTHON
 Divcion = 45/12
```

```PYTHON
operacion=(45+12+23)/4
op=15+12+14+13/4
#Presedencia de operadores
```
### OPERADORES DE  DE USO ESPECIAL
```PYTHON
# OPERADOR DE USO ESPECIAL (SUMA)
suma=45+47 # Operador suma resultado 87
suma='45' + 12 # Operador  concatenacion resultado 4512
saludo= 'Hola'+'Mundo' # concatenacion HolaMundo
saludo2='Hola'+''+'Mundo' # concatenar Hola Mundo
# OPERADOR DE USO ESPECIAL (MULTIPLICAR)
saludos='hola'*2 #holahola
saludo1s='hola '*2 #hola hola
```


## DATOS ESTRUCTURADOS

## LISTAS
Se puede almacenar distintos tipos de datos en una sola lista separados por coma.

```PYTHON
 Lista=['nombre',10, False]
 Lista_amigos=['jory','ñawi','adan','chinita']
```
## OBJETOS

Tambien al ygual que las listas almacenas distintos tipos de dstos, pero con un orden.

Para almacenar datos de un objeto nesesitamos especificar in indice y un valor indice →valor
```PYTHON
{
    'nombre':'jory',
    'edad':54
    'sexo' : 'todos los dias'
}
###################################
#combinar ambas estructura de datos
alumno={
    'nombre':'jory',
    'edad':54
    'amigos': [ 'antony','edwin','china'],
    'direccion':{
        'departamento': 'ayacucho',
        'provincia': 'lucanas',
        'distrito': 'puquio',
        'jiron': ' cusco',
        'numero':125

    }
}
 alumnos=[{},{},{}]
```
## CONTROLES DEN FLUJO
### DECISIONES
Solo se ejecuta el codigo si cumple la condicion es verdadera,  podemas hacer si la condicion sea falsa se ejeute otro codigo.

**SINTAXIS**

Primero especificar el codigo que ejecutara si cumple una condicion
```PYTHON
if <condicion>:
    ## El codigo que deseamos ejecutar si la condicion es verdad
    print('Ejecuta esto')
## Aqui estamos fuera del if o del si este codigo siemprese ejecutara no depende del if
print('Esto siempre ejecutara')
#---------------------------------------------------------------------
# Si queremos que se ejecute un codigo en caso sea falso
if <condicion falsa>:
    print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
```
**EJEMPLITOS**

```PYTHON
if 15>18:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
if 15*2==30:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
condicion= True
if  condicion:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```



## CICLOS
**EXISTEN  DOS TIPOS**

* Cuando sabemos la cantidad de veses que vamos a repetir algo.
Para este caso existe el **FOR**. Sintaxis despues de la palabra reservada **FOR**  deberemos crear una variable que almacene el numero que iremos intentando.luego tendremos que indicar el rango a intentar a los elementos a intentar.
```PYTHON
for i in range(1,5):
    print(i)
```
```PYTHON
vocales=['a','e','i','o','u']
for i in vocales:
    print (i)
```
```PYTHON
numeros=['45','12','78','1','2']
for i in numeros:
    print (i)
```


* Cuando no sabesmos la cantidad de veses que vamos a repetir algo.


 **WHILE**
```PYTHON
condicion= true
while condicion:
   print('hola')
   texto=input('Ingresa un nombre o salir para salir del programa: ')
   if true texto=='salir' :
   condicion False
```

## FUNCIONES
**Existen dos funciones**
1. Propias de lenguaje
   
   Que ya vienen creadas ye insertadas en **PYTHON**  y estan listas para ser usadas

   *Estructura de uso de una funcion*
    
    tiene el nombre seguido de parentises
    dentro de paretisis ódemos pasarle datos que nesesita la funcion para ejecutarse
    . Esta funcion que nos sirve para  para mostar por consola de datos.
```PYTHON
print ('hola')
```
**LEN**

Esta funcion nos permite saber la longuitud de una lista o un strung **LEN** nos debuelve un numero
```PYTHON
print (len([1,5,6,7,8]))
```
**INPUT**

Es una funcion que se detiene a esperar que el usuario introdusca informacion
Entre parentisis podemos escribir un mensaje que indique la accion que realizara el usuario.
```PYTHON
input('INGRESA INGRESA: ')
```
**MAX**
Esta funcion nos muestra el numero mayor de una lista 
```python
lista [45,12,78,9,6,12]
numero_mayor=max(lista)
print( numero_mayor)
```
**MIN**

Esta funcion nos muestra el numero mENOR de una lista 
```python
lista [45,12,78,9,6,12]
numero_menor=min(lista)
print( numero_menor)
```
**STRING**

Funcion para combertir una string a un numero entero
```python
numero_string='100'
print(type(numero_string))
numero_entero=int(numero_string
print(type(numero_entero)))
```
```python
int ('100') # → 100 es un nujmero entero
```
Funcion para combertir un entyero a un string
```python
str ('100') # → 100 es un numerostring
```
**APPEND**

Funcion que nos permite agregar elementos al final de una lista
```python
lista=[15,12,78]
elemento=100
lista.append(elemento)
print (lista)
```
**POP**

Funcion de pythpn que nos permite eliminar los elementos que se encuentra al final de la lista
```python
lista=[15,12,78]
lista.pop(elemento)
print(lista)
```

**INSERT**

Funcion de python que nos permiteagregar elementos en cualquier posiscion de mi lista para eso se le tiene que pasar dos parametros, primero indicarles el indice y segundo el dato qye se va agregar
```python
lista_nombre['feli','nando','nadine','bichota']
lista_nombre.insert(1,'satanas')
print(lista_nombre)}
```
**REMOVE**

Funcion de python que nos permite eliminar elemenos de cualquier posiscion de una lista, esta funcion resibe solo elemento que deseamos eliminar.
```python
lista=[4,5,6,7,8,9]
lista.remove(6)
print(lista)


```
**SPLIT**


Funcion que nos permite dividir una lista una cadena

```python
cadena='hola como estan'
lista=cadena.split()
print(lista)
url='www.google.com/id=70133573'
id=url.split('=').pop()
print(id)
```



2. Funciones creadas
     
   Una funcion son mimi programas tambien se les conose como modulos mo fragmentos de codigo de uso exclusivo

   **FUNCIONES PROPIAS**

   PASOSPARA CREARA UNA FUNCION PROPIA*

    1. Hacer uso de la palabra reservada    **DEF**
    2. Defenir un nombre de funcion que describa que tarea va realizar
    3. Establecer los parametros qe revisara la funcion entre parentisis().
    4. Establecer que valor o dato retornara mi funcion con la palabra reservada **return**
   **OBSERVACION**: Tambien  podemos hacer uso de la funcion **print** para retomar un mensaje en nuestra funcion.
   Existen dos tipos de funciones los que que no reciven ningun parametro
   *Ylos que reciben  parametros*
   ```python
   def saludo():
    print('hola este es un saludo')

   ```
  *Caomo hacemos la funcion?*
  *nombre de la funcion y parentisis*

   **FUNCION CON PATAMETROS**
   ```PYTHON
   def mi_print(texto):
    print(texto)
    print('Hola este es un print de python')
    print('Hola este es mi print creado')
   ```


   PASOSPARA CREARA UNA FUNCION PROPIA*

 1. Hacer uso de la palabra reservada    **DEF**
 2. Defenir un nombre de funcion que describa que tarea va realizar
 3. Establecer los parametros qe revisara la funcion entre parentisis().
 4. Establecer que valor o dato retornara mi funcion con la palabra reservada **return**
   **OBSERVACION**: Tambien  podemos hacer uso de la funcion **print** para retomar un mensaje en nuestra funcion.
   Existen dos tipos de funciones los que que no reciven ningun parametro
   *Ylos que reciben  parametros*
   ```python
   def saludo():
    print('hola este es un saludo')

   ```
  *Caomo hacemos la funcion?*
  *nombre de la funcion y parentisis*

   **FUNCION CON PATAMETROS**
   ```PYTHON
   def mi_print(texto):
    print(texto)
    print('Hola este es un print de python')
    print('Hola este es mi print creado')
   ```


```python
def suma(a,b):
    total=a+b
    return total
mi_print(suma(45,12)) ## →................. 57
 
```



**EJEMPLO**

Parra que se usa esta funcion?
para mostrar el valor maximo de una lista

```python
lista=[12,4,45,78,3,1]
mi_print(max(lista)) ## →................78

def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
       if numero > numero_mayor
        numero_mayor=numnero
    return numero_mayor
mi_print(mi_max(lista))
    
```
Parra que se usa esta funcion?
para mostrar el valor minimo de una lista

```python
lista=[12,4,45,78,3,1]
mi_print(min(lista)) ## →................78

def mi_min(lista):
    numero_menor=lista[0]
    for numero in lista:
       if numero < numero_menor
        numero_menor=numnero
    return numero_menor
mi_print(mi_min(lista))
    
```

**FUNCION CON MUCHOS PARAMETROS
```PYTHON
def funcion(*muchos parametros):
   total=0
   for numero in muchos parametros:
    total=total+numero
   return total
print( funcion(45,12,78,10,20))
```

```python
def datos(*args):
    nombre=args[0]
    apellido=args[1]
    edad=args[3]
    return f'mi nombre es,{nombre},{apellido},y mi edad es,{edad}'
    print(datos('edwin','ramos','34'))
```
**(*)args**
combierte
