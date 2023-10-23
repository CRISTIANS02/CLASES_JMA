

import random

categorias = ['abarrotes', 'farmacia', 'bodega', 'restaurant']
gerentes = ['edwin', 'china', 'christian', 'nadine']

tiendas = [
  {'ruc': '10714504431', 'nombre': 'Los Hermanos', 'categoria': random.sample(categorias, 2), 'horario_atencion': {'turno_mañana': '7am-12m', 'turno_tarde': '2pm-8pm'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10751204690', 'nombre': 'FarmaDiego', 'categoria': random.sample(categorias, 3), 'horario_atencion': {'turno_mañana': '8am-1pm', 'turno_tarde': '3pm-9pm'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10722302580', 'nombre': 'Pizza Mia', 'categoria': random.sample(categorias, 4), 'horario_atencion': {'turno_mañana': '10am-3pm', 'turno_tarde': '6pm-11pm'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10142378965', 'nombre': 'Don Pepe', 'categoria': random.sample(categorias, 2), 'horario_atencion': {'turno_continuo': '24 horas'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10659874531', 'nombre': 'El Super', 'categoria': random.sample(categorias, 3), 'horario_atencion': {'turno_mañana': '7am-1pm', 'turno_tarde': '4pm-9pm'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10741258963', 'nombre': 'La Esquina Fresca', 'categoria': random.sample(categorias, 2), 'horario_atencion': {'turno_mañana': '7:30am-2:30pm'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10755489632', 'nombre': 'El Rinconcito', 'categoria': random.sample(categorias, 3), 'horario_atencion': {'turno_noche': '6pm-3am'}, 'gerente': random.choice(gerentes)},  
  {'ruc': '10236587456', 'nombre': 'Sabores', 'categoria': random.sample(categorias, 2), 'horario_atencion': {'turno_mañana': '9am-2pm', 'turno_tarde': '5pm-10pm'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10785421596', 'nombre': 'La Despensa', 'categoria': random.sample(categorias, 4), 'horario_atencion': {'turno_continuo': '24 horas'}, 'gerente': random.choice(gerentes)},
  {'ruc': '10412032589', 'nombre': 'El Mesón', 'categoria': random.sample(categorias, 3), 'horario_atencion': {'turno_noche': '6pm-2am'}, 'gerente': random.choice(gerentes)}  
]

class Tiendas:

  def tiendas_por_gerente(self, gerente):
    return [tienda for tienda in tiendas if tienda['gerente'] == gerente]

  def tiendas_mas_2_categorias(self):
    return [tienda for tienda in tiendas if len(tienda['categoria']) > 2]
  
  def nombre_ruc(self):
    return [{ 'nombre': tienda['nombre'], 'ruc': tienda['ruc']} for tienda in tiendas]

tienda = Tiendas()
print(tienda.tiendas_por_gerente('edwin')) 
print(tienda.tiendas_mas_2_categorias())
print(tienda.nombre_ruc())