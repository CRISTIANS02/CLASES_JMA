from bd import *

class Tiendas_comerciales:

  def tienda_gerente(self, bd_negocios, nombre_gerente):
    respuesta = list(filter(lambda el: el['gerente'] == nombre_gerente, bd_negocios))
    return respuesta

  def tiendas_mas_Categorias(self, bd_negocios):
    respuesta = list(filter(lambda el: len(el['categoria']) > 2, bd_negocios))
    return respuesta

  def ruc_nombre(self, bd_negocios):
    respuesta = list(map(lambda el: {"nombre_negocio": el['nombre'], "ruc_negocio": el['ruc']}, bd_negocios))
    return respuesta

  def eliminar_negocio(self,id):
    eliminar_negocio= negocios.pop(id-1)
    return f" el sigiente producto fue eliminado{eliminar_negocio}"

  def actualizar_tienda(self, id, clave, valor):
    ol=valor
    actualizar_tienda=list(filter(lambda obj:obj[clave]==id,negocios))[0].update({clave:valor})
    return " se actualizo satisfactoriamente"
  
  def borrar(self,ruc):
    rc=list(filter(lambda el:el['ruc']!=ruc,negocios))
    return rc
  
  
  def crear_nuevoProd(self, bd_negocios, negocio):
    bd_negocios.append(negocio)
    return bd_negocios

  def actualizar_horaAtencion(self,id,clave,valor):
    negocios[id-1][clave]=valor
    return " llego la actualizacion del horario"
  


  def mostrar_todo(self, bd_negocios):
    print(bd_negocios)

gerente = Tiendas_comerciales()

#print(gerente.tienda_gerente(negocios, 'edwin')) 

#print(gerente.tiendas_mas_Categorias(negocios))

#print(gerente.ruc_nombre(negocios))

#print(gerente.eliminar_negocio(negocios, 10714504431))

#print(gerente.actualizar_tienda(negocios, 10758962451, 'horario_atencion', {'nuevo': 'horario'}))

#print(gerente.crear_nuevoProd(negocios, {'ruc': '100000000003', 'nombre': '365'}))

print(gerente.actualizar_horaAtencion(negocios, 10714504431, {'turno_noche': '12am - 5am','dia':'3pm-9pm'})) 


# print(gerente.mostrar_todo(negocios))





