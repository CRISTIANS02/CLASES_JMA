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

  def eliminar_negocio(self, bd_negocios, ruc):
    respuesta = list(filter(lambda el: el['ruc'] != ruc, bd_negocios))
    return respuesta

  def actualizar_tienda(self, bd_negocios, ruc, clave, valor):
    for negocio in bd_negocios:
      if negocio['ruc'] == ruc:
        negocio[clave] = valor
    return bd_negocios

  def crear_nuevoProd(self, bd_negocios, negocio):
    bd_negocios.append(negocio)
    return bd_negocios

  def actualizar_horaAtencion(self, bd_negocios, ruc, nuevo_horario):
    for negocio in bd_negocios:
      if negocio['ruc'] == ruc:
        negocio['horario_atencion'] = nuevo_horario
    return bd_negocios

  def mostrar_todo(self, bd_negocios):
    print(bd_negocios)

gerente = Tiendas_comerciales()

print(gerente.tienda_gerente(negocios, 'edwin')) 

print(gerente.tiendas_mas_Categorias(negocios))

print(gerente.ruc_nombre(negocios))

print(gerente.eliminar_negocio(negocios, 10714504431))

print(gerente.actualizar_tienda(negocios, 10758962451, 'horario_atencion', {'nuevo': 'horario'}))

print(gerente.crear_nuevoProd(negocios, {'ruc': '105589654123', 'nombre': 'Nueva Tienda'}))

print(gerente.actualizar_horaAtencion(negocios, 10714504431, {'turno_noche': '12am - 5am'})) 

print(gerente.mostrar_todo(negocios))





