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

for n in range (1,6):
        nombre=input('Ingrese  un nombre: ')
        print(f'ingresaste {n} veses el nombre: ')


nombres = {}

for _ in range(5):
    nombre = input("Ingrese un nombre: ")
    if nombre in nombres:
        nombres[nombre] += 1
    else:
        nombres[nombre] = 1

for nombre, cantidad in nombres.items():
    print(f"El nombre {nombre} fue ingresado {cantidad} veces.")


#crear un programa que pida el numero y lo evalue con el numero premiado, si el numero ingresado es el premiado el programa finalizara 
# si el numero ingresado es incorrecto el programa segira pediendo el numeropremiado