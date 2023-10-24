#tarea
## crear una lista con 10 objetos que obtenga los adatos de las tiendas comerciales
#ejemplo:
# tiendas=[
#     {
#         'ruc':'10714504431',
#         'nombre': ' the brothers',
#         'categoria':['abarrotes','bodega'],
#         'horario_atencion':{
#              'turno_mañana':7am-12m,
#              'turno_tarde':2pm-8pm
#         },
#         'gerente':'manuel'
#     }
# ]
# observacion1:
# las categorias sera de 4: abarrotes, farmacia,bodega,restaurant.
#Observacion2:
#Los gerentes solo podran ser los siguientes: edwin,china,crhistian,nadine
# realizar los siguientes ejercicios
# crear la clase para tiendas que tenga los siguientes metodoso uso de caso
 #1. crear un metodo que me filtre las tiendas que tiene cada gerente
 #2. crear un metodo que me muestre los negocios que tienen mas de dos categorias
 #3. crear un metodo que me muestre solo el nombre y ruc de las tiendas.
# Ejemplo de uso
from bd import *
class Tiendas2023:
    
    def tienda_gerente(self,bd_tiendas,nom_gerente):
        tiendita=list(filter(lambda el:el['gerente']==nom_gerente,bd_tiendas))
        return tiendita
    
    def negocios_con_mas_categorias(self,bd_tiendas):
        tiendita=list(filter(lambda el:len(el['categoria'])>2,bd_tiendas))
        return tiendita
    
    def ruc_nombre(self,bd_tiendas):
        tiendita=list(map(lambda el: {
            "nombre_negocio":el['nombre'],
            'ruc_negocio':el['ruc']
            },bd_tiendas))
        
    def eliminar_negocio(self,bd_tiendas,ruc):
        tiendita=list(filter(lambda el:el['ruc']!=ruc,bd_tiendas))
        return tiendita.index
        
    # tarea 
    def actualizar_negocio(sefl):
        pass
    
    # otro metodo para crear un nuevo producto
    
    
    # otro metodo para actualizar el horario de atencion
    
    
    
    def mostrar_todo(self):
        pass
        
  
   
gerente=Tiendas2023()
print(gerente.tienda_gerente(tiendas,'china'))
print(gerente.negocios_con_mas_categorias(tiendas))
print(gerente.mostrar_nombre_ruc(tiendas))
print(gerente.eliminar_negocio(tiendas,12345678901))







 
