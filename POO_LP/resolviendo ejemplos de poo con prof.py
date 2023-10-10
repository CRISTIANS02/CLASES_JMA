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
    

    