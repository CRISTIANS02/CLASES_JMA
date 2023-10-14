# PROGRAMACION ORIENTADA  A OBJETOS
## **EN INGLES ES OBJECT ORIENT PROGRAMING**
Es un paradigma de programacion

**paradigma**.- es un modelo,patron o ejemplo que se debe segir

**POO**  .- Es un modelo de como podermos programar
**Objetivo**- El  objetivo es organizar el codigo de manera que se asemeja a como pensamos en la  vida real

se basa en Objetos y en la **POO** un objeto es toda identidad que se puede escribir atravez de **atributos**
 y **funciones** que puede realizar  la edintidad

# ATRIBUTOS DE CLASE Y ATRIBUTOS DE INSTANCIA
 **EJEMPLOS N°1**
```PYTHON
# 1  celulares
class Celular:
    #atributos de tipo clase= eso quiere decir que son iguales para todo los objetos
    familia='SmartPhone'
    #atributos de instancia
    # son atributos  propios del objeto
    # crearemos una funcion inicializadora
    def __init__(self,marca,modelo,emei,nroCelular):  
        self.marca=marca  
        self.mmodelo=modelo
        self.memei=emei 
        self.mnroCelular=nroCelular 
    
    #funciaonalidades
    def  llamar(self,destino):
        return f'llamando a: {destino}'
    
    
#Objeto celular jory
llamandojory=Celular('SM','A726B','95874125896','963258741') # instanciando mi clase, creando mi objeto celular
print(llamandojory.marca)
print(llamandojory.familia)
print(llamandojory.llamar('china'))
    
 # Objeto celular nadine
llamandoNadine=Celular('SM','A526B','95874125896','963258741') # instanciando mi clase, creando mi objeto celular
print(llamandoNadine.marca)
print(llamandojory.familia)
print(llamandoNadine.llamar('china'))
    
```