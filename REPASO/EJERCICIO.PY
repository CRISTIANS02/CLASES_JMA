## FOR 
# ## Crear un programa que me pida edad de una persona, 
# si la edad es mayor a 18 que muestre un menssaje 'Eres mayor de edad'
#caso contrario que muestre un mensaje 'Eres menor de edad'.


# nombre=input(' Ingrese su nombre: ')
# edad = int(input("Ingresa tu edad: "))
# if edad>=18:
#         print( nombre + ' ' + 'Eres mayor de edad')
# else:
#     print(nombre + ' ' +'Eres menor de edad')
    
 



# Una tienda comercial desea hacer un descuento del 20%, crear un programa  que me determine si el cliente se hace acreedor
#del descuento teniendo en cuenta los  siiguiente: si el cliente realiza una compra de ygual o mayor a s/. 1000 soles  mostrar un mensaje que diga 
# 'GANASTE EL DESCUENTO DE20%, AHORA PAGARAS <mostar el total de   la compra menos el descuento>' en caso la compra o supere los S/.1000 soles  entonses 
#mostrar un mensaje que diga'NO APLICAS AL DESCUENTO <mostar el monto de la compra'



# NOM_TIENDA= "COMERCIAL JUELICIANA "
# NOM_CLIENTE=input ('Ingrese su nombre: ')
# MONT_COMPRA= int(input('Ingresa el monto de compra: '))
# if MONT_COMPRA>= 1000:
#         descuento = MONT_COMPRA * 0.2
#         total_pagar = MONT_COMPRA - descuento
#         print(f"¡GANASTE EL DESCUENTO DE 20%! Ahora pagarás {total_pagar} soles.")
# else:
#         print(f"NO APLICAS AL DESCUENTO. El monto de la compra es de {MONT_COMPRA} soles.")

        

# WHILE
##  Crear un programa que me pida 5 veses un nombre y por cada que lo pida muestra 
# la cantidad de veses que ingreso el nombre


# NOM_CLIENT1=input ('Ingrese su nombre: ')
# for _ in range(6):

# for n in range (1,6):
#         nombre=input('Ingrese  un nombre: ')
#         print(f'ingresaste {n} veses el nombre: ')


# nombres = {}

# for _ in range(5):
#     nombre = input("Ingrese un nombre: ")
#     if nombre in nombres:
#         nombres[nombre] += 1
#     else:
#         nombres[nombre] = 1

# for nombre, cantidad in nombres.items():
#     print(f"El nombre {nombre} fue ingresado {cantidad} veces.")


#crear un programa que pida el numero y lo evalue con el numero premiado, si el numero ingresado es el premiado el programa finalizara 
# si el numero ingresado es incorrecto el programa segira pediendo el numeropremiado

# nombre =input('Ingrese su nombre: ')
# numero_premiado = 1234

# while True:
#     numero = int(input("Ingrese un número: "))
#     if numero == numero_premiado:
#         print( nombre + "¡Felicidades! Has ingresado el número premiado.")
#         break
#     else:
#         print(f"{nombre} Número incorrecto. Sigue intentando.")

# ejercicio n°

# crear una funcion por cada operacion aritmetico que resiva dos parametros y  retorne el resultado de la operacion. OJO.
# crearse una funcion que nos permita imprimir el resultado


# ## DATA

# num1=int(input('INGRESE EL PRIMER NUMERO :'))
# num2=int(input('INGRESE EL SEGUNDO  NUMERO :'))
# ## SUMA

# def suma(num1,num2):
#     total=num1+num2
#     return total
# #print(suma(num1,num2)) 
 
# ## RESTA
# def resta(num1,num2):
#     total=num1-num2
#     return total
# #print(resta(num1,num2)) 

# ## MULTIPLICAR
# def multi(num1,num2):
#     total=num1*num2
#     return total
# #print(multi(num1,num2))


# ## DIVICION
# def dividir(num1,num2):
#     total=num1/num2
#     return total
# #print(dividir(num1,num2))


# # Realizar la suma
# resultado_suma = suma(num1, num2)
# print(resultado_suma)

# # Realizar la resta
# resultado_resta = resta(num1, num2)
# print(resultado_resta)

# # Realizar la multiplicación
# resultado_multiplicacion = multi(num1, num2)
# print(resultado_multiplicacion)

# # Realizar la división
# resultado_division = dividir(num1, num2)
# print(resultado_division)




# ejercicion°

# escribe una funcion que reciba un numero entero posisivo y devuelva su faactorial


    

# def factorial(n):
#     if n < 0:
#         return "El número debe ser positivo."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         resultado = 1
#         for i in range(2, n+1):
#             resultado *= i
#         return resultado
    


# numero = int(input('INGRESE EL NUMERO PARA EVALUAR LA POTENCIA: '))
# resultado_factorial = factorial(numero)
# print("El factorial de", numero, "es:", resultado_factorial)

## escribir una funcion que resiba com parametros una lista de numeros y retorne 
# una nueva lista con el cuadro de cada numero de la lista ingresada.

# def obtener_cuadrados(lista):
#     cuadrados = [num ** 2 for num in lista]
#     return cuadrados

# # Ejemplo de uso:
# numeros = [1, 2, 3, 4, 5]
# lista_cuadrados = obtener_cuadrados(numeros)
# print(lista_cuadrados)


## Escribir un programa que reciba una cadena de caracteres y debuelva un objeto con cada palabra que contiene y su frecuencia
def contar_frecuencia_palabras(cadena):
    frecuencia_palabras = {}
    palabras = cadena.split()

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras

# Ejemplo de uso:
cadena = "Hola mundo, hola de nuevo"
resultado = contar_frecuencia_palabras(cadena)
print(resultado)